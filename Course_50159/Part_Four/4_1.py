#Напишите программу, которая в последовательности натуральных чисел вычисляет сумму всех трехзначных чисел, 
#кратных 3 и оканчивающихся на 2. 
#Программа получает на вход натуральные числа, количество введённых чисел неизвестно, 
#последовательность чисел заканчивается числом 0 (0 – признак окончания ввода, не входит в последовательность).
#Количество чисел не превышает 1000. Введённые числа не превышают 30 000.
#Программа должна вывести два значения в двух строках.
#Первое значение: сумму всех трехзначных чисел, кратных 3 и оканчивающихся на 2, или вывести «NO», если таких чисел нет.
#Второе число: если есть хотя бы одно трёхзначное число кратное 3 и оканчивающиеся на 2, 
#программа должна вывести второе число - максимальное число среди всех введенных
#трехзначных чисел кратных 3 и оканчивающихся на 2. 
#Если выведено «NO», то вывести вторым числом минимальное число среди всех введенных чисел в последовательности.
counter = ""
tmin = 30000
total = 0
tmax = 0
result = ""
while counter != 0:
    counter = int(input())
    if counter == 0:
        break
    if counter >= 100 and counter < 1000 and counter % 3 == 0 and counter % 10 == 2:
        total += counter
        if counter > tmax:
            tmax = counter
    if counter < tmin:
        tmin = counter
if total == 0:
    total = "NO"
    result = tmin
else:
    result = tmax
print(total)
print(result)