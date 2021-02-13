#открываем файл #abc a bCd bC AbC BC BCD bcd ABC
#прочитать с помощью цикла
#преоброзовать сначала в список, затем в словарь(комбинация = ключ, значение = количество повторов)#{aa: 2, ab: 2, c: 1}
#перебрать полученный словарь, сравнить число повторений и если они одинаковы, вывести то что по алфавиту раньше 
#записать полученную комбинацию и количество раз 
#Недавно мы считали для каждого слова количество его вхождений в строку.
#Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

#Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
#и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
#Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

#В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.
with open("dataset_3363_3.txt", "r") as information, open("output.txt", "w") as output:
    dictionary = {}
    max_value = 1
    max_key = ""
    for line in information:
        _list = line.strip().lower().split(" ")
        for i in _list:
            if i in dictionary: 
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
        elif value == max_value:
            if key > max_key:
                max_key = key
    output.write(max_key + " " + str(max_value))