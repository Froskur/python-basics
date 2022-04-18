#!/usr/bin/env python
# coding: utf-8

# # 1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
# 
# 

# In[10]:


userAge = 30
print(userAge)


# In[16]:


addressCity = "NY,aveny Lennia 4"
print(f"Your adress: {addressCity}")


# In[32]:


nameCity = None

while not(nameCity): 
    nameCity = input(f'Ener your location?')
    
print(f'You enter location: {nameCity}')


# # 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# In[66]:


secondCount = 0
secondMin   = 1000

while (secondCount < secondMin): 
    secondCount = int(input(f'Enter the number of seconds (value must be greater than {secondMin})'))

myHour  = secondCount // (3600)
myMinut = (secondCount-myHour*3600) // 60
mySec   = secondCount - myHour*3600 - myMinut*60

print('Long time HH:MM:SS = {:02d}:{:02d}:{:02d}'.format(myHour, myMinut, mySec))


# # 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# In[75]:


n = input('Your number:')
total = int(n)+int(n*2)+int(n*3)
print(f'{n} + {n*2} + {n*3} = {total}') 


# # 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
# 

# In[100]:


myNumber = ''
countMin = 6

# используем ленивый or, чтобы не было ошибки 
while ((len(myNumber) < countMin) or (int(myNumber) <= 0)): 
    myNumber = input(f'Please enter a positive integer (minimum {countMin} characters)')
    
# теперь найдем большое самое большое число, хотя While конечно не удобен тут
maxNumber = i = 0;
while i < len(myNumber) :
    if maxNumber < int(myNumber[i]):
        maxNumber = int(myNumber[i])

    i += 1

print(f'In the number {myNumber}, the largest number is {maxNumber}')


# # 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

# In[114]:


myRevenu = input("Company revenue?:")
myCosts  = input("Company costs?:")

myResult = int(myRevenu) - int(myCosts) 
if myResult > 0:
    print(f'Congratulations, your profit: {myResult}')
elif myResult < 0:
    print(f'Your loss: {myResult*-1}')
else:
    print(f'You have worked to zero')


# # 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

# In[128]:


numberEmployees = int(input('The number of employees?'))


if myResult > 0:
    print('Your ROI: {:.2%}'.format(int(myResult)/int(myRevenu)))

if numberEmployees > 0:
    print('Profit per employee: {}'.format(int(myResult)/numberEmployees))
    


# # 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

# In[132]:


a = 3
b = 8
counter = 1

while (a <= b):
    a += a * .1
    counter += 1
    
print (f'На {counter} день спортсмен достигнет результата {a} км. Это больше чем порог {b} км.')    

