# 4.	Имеются два списка состоящие из произвольных элементов.
# Напишите функцию которая возвращает пересечение списков (элементы которые встречаются в и там и там)

def intersection_of_lists(list1, list2):
    return list(filter(lambda x: x in list2, list1))

list1 = [1, 2, "Девять", 4, 5]
list2 = [4, 'Девять', 6, 7, 1]
result_intersection = intersection_of_lists(list1, list2)
print(result_intersection)