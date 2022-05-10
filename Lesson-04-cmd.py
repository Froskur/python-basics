#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sys import argv

#### 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. 
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта 
# для конкретных значений необходимо запускать скрипт с параметрами.

if ( len(argv) < 3) or (len(argv) > 4):
    print("Для запуска используйте запуск из CMD такого вида: script.py <выработка> <ставка> <премия> . Премия может быть не указана")    
    exit(0)


if (len(argv) == 3 ):
    premium = 0
    _, production, rate  = argv
else:
    _, production, rate, premium = argv


#Валдиация всего и вся    
try:
    production = int(production)    
except:
    print("Выроботка должна быть указана в часах")
    exit(0)

try:
    rate = float(rate)    
except:
    print("Ставка в час должна быть вещественным числом")
    exit(0)
 
try:
    premium = float(premium)    
except:
    print("Если премия указана она должна быть вещественным числом")
    exit(0)
 
#Всё готов можно делать расчёт
salary = production*rate + premium    
print(f'ЗП сотрудника  = {salary:,.2f}')    

