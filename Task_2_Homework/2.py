# 2.	Имеется список, состоящий из чисел.
# Напишите функцию которая принимает число и возвращает список состоящий из элементов первого списка кратных входному параметру.

def find_numb(numbers, div):
    return list(filter(lambda x: x % div == 0, numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
div = 4
result = find_numb(numbers, div)
print(result)