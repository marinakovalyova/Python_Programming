#Напишите программу, которая в последовательности натуральных чисел определяет минимальное число,
#оканчивающееся на 4. Программа получает на вход количество чисел в последовательности, а затем сами числа.
#В последовательности всегда имеется число, оканчивающееся на 4.
#Количество чисел не превышает 1000. Введённые числа не превышают 30 000.
#Программа должна вывести одно число – минимальное число, оканчивающееся на 4.
counter = int(input())
xmin = 30000
for i in range(counter):
	number = int(input())
	if number < xmin and number % 10 == 4:
		xmin = number
print(xmin)