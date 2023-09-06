# 8.	* Пусть у нас есть список кортежей, которые описывают химические элементы (номер группы, порядковый номер, название)
#
# elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
#
# Отсортируйте список не учитывая при сортировке первый элемент каждого кортежа.


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]


modified_elements = list(map(lambda x: (x[1], x[2]), elements)) # преобразование списка кортежей в список кортежей без первого элемента.

print(modified_elements)

sorted_elements = sorted(modified_elements, key=lambda x: (x[0], x[1])) # Отсортировали по порядковому номеру

print(sorted_elements)

restored_elements = list(map(lambda x: next(filter(lambda y: y[1] == x[0] and y[2] == x[1], elements)), sorted_elements))  #восстановили исходные кортежи на основе отсортированного списка.

print(restored_elements)