def square(number):
    return number**2


numbers=[1,2,3,4,5]
print(list(map(square,numbers)))

str_nums=['4','8','6','5','3','2','8','9','2','5']
print(list(map(int,str_nums)))


# Задача
# Имеется строка
# Напишите сопоставление которое возвращает список состоящий из букв исходной строки, в верхнем регистре.

string_upper = 'Mapping'
print(list(map(lambda x: x.upper(), string_upper)))

string_upper = 'Mapping'
print(''.join(list(map(lambda x: x.upper(), string_upper))))


# Задача
# Имеется список, состоящий из слов.
# Напишите сопоставление которое возвращает список длин строк исходного списка.

words = ['abs','len','filter','map','join']

print(list(map(len, words)))
