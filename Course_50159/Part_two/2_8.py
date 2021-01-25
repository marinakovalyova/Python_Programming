#Напишите программу для решения следующей задачи.

#Ученики 9 класса вели дневники наблюдения за погодой и ежедневно записывали дневную температуру.

#Найдите минимальную температуру для дней, когда столбик термометра поднимался выше нуля градусов. 
#Определите количество таких дней. Гарантируется, что за время наблюдения хотя бы
#в один из дней температура поднималась выше нуля градусов.

#Программа получает на вход количество дней, в течение которых проводилось наблюдение N (1≤N≤30),
#затем для каждого дня вводится температура. 
#-1 0 2 2 1 0 1 
days = int(input())
tmin = 10 ** 8
total = 0 
for _ in range(days):
    temperature = int(input())
    if temperature < tmin and temperature > 0:
        tmin = temperature
        total = 1
    elif temperature == tmin:
        total += 1
print(tmin)
print(total)