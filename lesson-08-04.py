# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod
import copy

class Storage():
    __dStorage = {
        'main':'Склад долго хранения',
        'shop1':'Склад розничного магазина',
        'opt':'Склад оптовых поставок',
        'defect':'Склад отдела брака'
    }

    __balances = {
        'main': [],
        'shop1': [],
        'opt': [],
        'defect': []
    }

    def supplay(self, storage=None, objAdd=None, count=1):
        if (storage==None) and (objAdd==None):
            print("Для обприходования надо передать первым аргументом код склада: "+",".join(self.__dStorage.keys())+"\n Вторым аргументом класс товара и третьем - количество")

        try:
            self.__dStorage[storage]
        except:
            print("Передан не правильный код склада, доступны:"+", ".join(self.__dStorage.keys()))
            return

        # Пока такая проверка
        if (type(objAdd) != Printer) and (type(objAdd) != Scanner) and (type(objAdd) != Copier):
            print("Передан не тот объект")
            return

        #Прошли, добавляем объект, так как это типа партионный учет добавляем столько объектов, сколько ввели
        self.__balances[storage].append({'item':objAdd, 'count':count})

    def getStorageStatus(self, storage=None):
        strorageShow = []
        if (storage):
            try:
                self.__dStorage[storage]
            except:
                print("Передан не правильный код склада, доступны:"+", ".join(self.__dStorage.keys()))
                return

            strorageShow.append(storage)
        else:
            strorageShow = self.__dStorage

        # Теперь пошли смотреть состояние:
        for stor in strorageShow:
            print(f"{self.__dStorage[stor]} ({stor}): { (str(len(self.__balances[stor]))+' позиций') if len(self.__balances[stor])>0 else 'пусто'}")
            if (len(self.__balances[stor])>0):
                for oneIntem in self.__balances[stor]:
                    print("  "+str(oneIntem['count'])+" шт. "+oneIntem['item'].getInfoFull())
                print("=====")

class OfficeApplinces(ABC):
    __title = None
    __model = None
    __manufacturer = 'NoName'
    __length = 0
    __width  = 0
    __height = 0

    def __str__(self):
        return self.getInfoFull()

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        if not(self.title):
            raise ValueError("При создании экземпляра обязательно указать title")

        self.model = kwargs.get('model')
        if not(self.model):
            raise ValueError("При создании экземпляра обязательно указать model")

        # Остальные не обязательны при создании
        self.manufacturer = kwargs.get('manufacturer','NoName')
        self.width = kwargs.get('width',  0)
        self.height = kwargs.get('height', 0)
        self.length = kwargs.get('length', 0)

    # Геттеры
    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def title(self):
        return self.__title

    @property
    def model(self):
        return self.__model

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # Виртуальные гетеры
    @property
    def size(self):
        return f"{self.width if self.width>0 else 'N'}x{self.height if self.height>0 else 'N'}x{self.length if self.length>0 else 'N'}".strip()

    # сеттеры

    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = str(value).strip();

    @title.setter
    def title(self, value):
        if (value):
            self.__title = str(value).strip().title();

    @model.setter
    def model(self, value):
        if (value):
            self.__model = str(value).strip().upper();

    @width.setter
    def width(self, value):
        if (isinstance(value, int)) and (value >= 0):
            self.__width = value
        else:
            raise ValueError("Ширина должна быть целым числом в миллиметрах. Если 0 - считается что не указана")

    @length.setter
    def length(self, value):
        if (isinstance(value, int)) and (value >= 0):
            self.__length = value
        else:
            raise ValueError("Длинна должна быть целым числом в миллиметрах. Если 0 - считается что не указана")

    @height.setter
    def height(self, value):
        if (isinstance(value, int)) and (value >= 0):
            self.__height = value
        else:
            raise ValueError("Высота должна быть целым числом в миллиметрах. Если 0 - считается что не указана")

    # Абстрактные интерфейсы
    @abstractmethod
    def getInfoFull(self):
        pass

    # Методы
    def getInfo(self):
        return f"{self.title} {self.model} ({self.manufacturer}) размеры (ШxВxГ): {self.size}"

    @staticmethod
    def getProp(v):
        if isinstance(v, bool):
            return f"{'ДА' if v else 'НЕТ' if v==False else 'Не указано'}"
        elif isinstance(v, list):
            return f"{','.join(v) if len(v)>0 else 'Не указано'}"
        else:
            return f"{str(v) if v else 'Не указано'}"


class Printer(OfficeApplinces):
    __speedPrint = None
    __pageSize = None

    __pageSizeIsset = ['A1','A2','A3','A4','A5','B2']

    def __init__(self, **kwargs):
        kwargs['title'] = "Принтер"
        self.speedPrint = kwargs.get('speedPrint')
        self.pageSize = kwargs.get('pageSize')
        super().__init__(**kwargs)

    @property
    def speedPrint(self):
        return self.__speedPrint

    @property
    def pageSize(self):
        return self.__pageSize

    @pageSize.setter
    def pageSize(self, value):
        if isinstance(value, str):
            self.__pageSize = [self.__setOneSizePage(value)]
        elif isinstance(value, list):
            self.__pageSize = []
            for one in value:
                self.__pageSize.append(self.__setOneSizePage(one))

    def __setOneSizePage(self, v):
        v = str(v)
        if self.__pageSizeIsset.count(v.strip().upper()) > 0:
            return v.strip().upper()
        else:
            raise ValueError("Передан неизвестный формат бумаги принтера, допустимы:" + ", ".join(self.__pageSizeIsset))

    @speedPrint.setter
    def speedPrint(self, value):
        if value:
            if isinstance(value, int):
                self.__speedPrint = value if value>0 else None
            else:
                raise ValueError("speedPrint (скорость печати) должна быть целым числом")

    def getInfoFull(self):
        tmpList = []
        tmpList.append("Скорость печати:"+OfficeApplinces.getProp(self.speedPrint)+" стр/мин")
        tmpList.append("Поддерживаемые форматы бумаги: " + OfficeApplinces.getProp(self.pageSize))

        return self.getInfo()+";  "+", ".join(tmpList)

class Scanner(OfficeApplinces):
    __manual  = None
    __maxLoad = None

    @property
    def manual(self):
        return self.__manual

    @property
    def maxLoad(self):
        return self.__maxLoad

    @manual.setter
    def manual(self, value):
        self.__manual = True if value else None if value == None else False

    @maxLoad.setter
    def maxLoad(self, value):
        self.__maxLoad = str(value) if value else None

    def __init__(self, **kwargs):
        kwargs['title'] = "Сканер"
        self.maxLoad = kwargs.get('maxLoad')
        self.manual = kwargs.get('manual')
        super().__init__(**kwargs)

    def getInfoFull(self):
        tmpList = []
        tmpList.append("Ручной:"+OfficeApplinces.getProp(self.manual))
        tmpList.append("Максимальная нагрузка: " + OfficeApplinces.getProp(self.maxLoad))

        return self.getInfo()+";  "+", ".join(tmpList)

class Copier(OfficeApplinces):
    __duplex  = None
    __network = None

    @property
    def duplex(self):
        return self.__duplex

    @property
    def network(self):
        return self.__network

    @duplex.setter
    def duplex(self, value):
        self.__duplex = True if value else None if value == None else False

    @network.setter
    def network(self, value):
        self.__network = True if value else None if value == None else False

    def __init__(self, **kwargs):
        kwargs['title'] = "копир"
        self.network = kwargs.get('network')
        self.duplex = kwargs.get('duplex')
        super().__init__(**kwargs)

    def getInfoFull(self):
        tmpList = []
        tmpList.append("Сетевой:"+OfficeApplinces.getProp(self.network))
        tmpList.append("Двусторонний:" + OfficeApplinces.getProp(self.duplex))

        return self.getInfo()+";  "+", ".join(tmpList)

# Просто отдельные объекты
mc = Printer(model="dn-4567", manufacturer="HP", width=300, length=500, pageSize=['A3','A4'])
print(mc)
print("====")

item2 = Copier(model="KX-56FG21", manufacturer="CANON", width=455, height=640, length=430, duplex=True)
print(item2)
print("====")

item3 = Scanner(model='NoName', manual=True, maxLoad='500 сканов в неделю')
print(item3)
print("====")

# теперь сам склад
s = Storage()
s.supplay('main', Printer(model="EJET-DK467", manufacturer="HP", width=300, length=500, pageSize=['A3','A4']), 4)
s.supplay('main', Printer(model="KXC-GF102", manufacturer="Kyocera", width=650, length=600, height=990, pageSize=['A2','A3','A4'], speedPrint=60), 10)
s.supplay('opt', Copier(model="KX-56FG21", manufacturer="CANON", width=455, height=640, length=430, duplex=True), 100)
s.supplay('shop1', Scanner(model='NoName', manual=True, maxLoad='500 сканов в неделю'), 5)
s.getStorageStatus()

# Движения по складу уже не делал, уж слишком муторно для тестовой задачи которая никому не пригодится.
