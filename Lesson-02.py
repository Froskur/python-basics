#!/usr/bin/env python
# coding: utf-8

# ### 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
# 

# In[52]:


myList = [45, 'Name', 0.34,(90,60,90),['Путь',14,'Река']]


# In[53]:


for num in range(len(myList)):
    tmpType = type(myList[num])
    if tmpType == list:
        print(f"Элемент {num} это список")
    elif tmpType == int:
        print(f"Элемент {num} это целое число")
    elif tmpType == str:
        print(f"Элемент {num} это строка")
    elif tmpType == tuple:
        print(f"Элемент {num} это кортеж")
    else:
        print(f"Ой, элемент {num} это {tmpType} и не знаю что с ним делать")

        


# ### 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

# In[46]:


maxValue = 0

while (maxValue <= 0):
    try:
        maxValue = int(input("Сколько значений в список будите вводить?"))
    except ValueError:
        pass

lstRecord = [] 

for num in range(maxValue):
    lstRecord.append(input(f"Введите {num} значение списка"))

lstRecordCoding = lstRecord.copy()    

for num in range(1,len(lstRecordCoding),2):
    lstRecordCoding.insert(num-1,lstRecordCoding.pop(num))

print(f'Ваш изначальный список: {lstRecord}')
print(f'Закодированный список: {lstRecordCoding}')
    


# ### 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

# In[56]:


lstSeason  = ['зима', 'весна', 'лето', 'осень']
dictSeason = {1:'зима', 2:'весна', 3:'лето', 4:'осень'}


# In[74]:


myMonth = 0

while not(0 < myMonth <= 12):
    try:
        myMonth = int(input("Введите число месяца: "))
    except ValueError:
        pass

#Сдвинем 12 месяц в 0 чтобы он попал в зиму
myMonth = myMonth if (myMonth<12) else 0

print(f'Сезон из списка: {lstSeason[myMonth//3]}')
print(f'Сезон из словаря: {dictSeason[myMonth//3+1]}')
    


# ### 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

# In[77]:


myStr = input("Введите строку (предложение) с пробелами и чтобы были слова более чем 10 символом, например - межконтинентальный:")
#myStr = 'Введите строку (предложение) с пробелами и чтобы были слова более чем 10 символом, например - межконтинентальный'


# In[91]:


tmp = myStr.split(' ')
for num in range(len(tmp)):
    print(f'{num+1}. {tmp[num][:10]}')


# ### 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

# In[103]:


myRate = [7, 5, 3, 3, 2]
newValue = 0

while (newValue<=0):
    try:
        newValue = int(input("Введите новое натуральное число для рейтинга: "))
    except ValueError:
        pass

#Не очень понял из задания, можно ли использовать сортировку, но предположил что да, так как не запрещено    
myRate.append(newValue)
myRate.sort(reverse=True)

print(f'Рейтинг: {myRate}')


# ### 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# 
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# 
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
# 
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# In[137]:


# Определим "колонки" нашей структры и типы ожидаемых данных 
itemParam = {'название':str,'цена':float,'количество':int,'eд':str}
allProducts = []


# In[124]:


newProduct = {}

while (True):
    for nameProp in itemParam:
        #Валидацию делать не стал, чтобы не заграмождать код
        if itemParam[nameProp] == int:
            newProduct[nameProp] = int(input(f'Введите числовое(целое) значение параметра **{nameProp}** для вашего товара: '))
        elif itemParam[nameProp] == float:    
            newProduct[nameProp] = float(input(f'Введите вещественное значение параметра **{nameProp}** для вашего товара: '))
        else:   
            newProduct[nameProp] = input(f'Введите строковое значение параметра **{nameProp}** для вашего товара: ')
            
    allProducts.append((len(allProducts)+1, newProduct))        
    
    if (str(input('Завести ещё? [да (д, yes,y)/нет (н, no, n)]: ')).lower() in ['нет','н','n','not','no']):
        break
        
print(allProducts)


# In[140]:


# Для дальнейши логики список проишем руками уже, вводить это руками - безумие 
allProducts = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
    (4, {'название': 'мышка', 'цена': 170, 'количество': 15, 'eд': 'шт.'}),
    (5, {'название': 'бумага', 'цена': 1100, 'количество': 100, 'eд': 'уп.'}),
    (6, {'название': 'монитор', 'цена': 23400, 'количество': 10, 'eд': 'шт.'}),
    (7, {'название': 'монитор', 'цена': 13050, 'количество': 40, 'eд': 'шт.'})
]


# In[142]:


# Соберем статистикку по продуктам
statProduct = {}

for nameProp in itemParam:
    statProduct[nameProp] = list(set([oneItem[1][nameProp] for oneItem in allProducts]))

print(statProduct)

