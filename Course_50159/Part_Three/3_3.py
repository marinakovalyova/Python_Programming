#Напишите программу, которая в последовательности чисел определяет минимальное четное число.
#Программа получает на вход целые числа, количество введённых чисел неизвестно, 
#последовательность чисел заканчивается числом 0 (0 — признак окончания ввода, не входит в последовательность).
#В последовательности всегда имеется четное число. Количество чисел не превышает 1000. Введённые числа не превышают 30 000.
#Программа должна вывести одно число — минимальное четное число
tmin = 30000
counter = ""
while counter != 0:
    counter = int(input())
    if counter == 0:
        break
    else:
        if counter < tmin and counter % 2 == 0:
            tmin = counter
print(tmin)