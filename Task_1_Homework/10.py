#Замените классическое представление цикла for в примере на любую конструкцию, так чтоб результат оставался тот же.

lst = [2,4,5,8,9,13]

for number in range(len(lst)):
    lst[number] *=number
    print(lst)


#Заменил цикл For на цикл While
lst = [2, 4, 5, 8, 9, 13]
index = 0

while index < len(lst):
    lst[index] *= index
    print(lst)
    index += 1
