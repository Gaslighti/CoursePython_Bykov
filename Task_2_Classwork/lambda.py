double=lambda x: x*2
print(double(5))

list_values=[1,3,4,2,6,7,5,8,9]

print(list(filter(lambda x: x%2 == 0, list_values)))

# Задача
# Имеется строка состоящая из нескольких слов.
# Напишите фильтр который возвращает список из букв строки, за исключением пробелов

my_str = 'lambda expressions'

print(list(filter(lambda x: x != ' ', my_str)))

#Задача
#Имеется список состоящий из элементов с разными типами данных.
#Напишите фильтр который выбирает только целые числа из исходного списка


list_values_two = [1,[1,2],'str',2,76.3,3]

print(list(filter(lambda x: isinstance(x,int), list_values_two)))

numbers = [1,2,4,5,7,8,10,11]

def filter_num(in_num):
    return in_num%2 == 0


print(list(filter(filter_num, numbers)))