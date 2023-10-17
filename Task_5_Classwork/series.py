import pandas as pd

my_series = pd.Series([2, 4, 6, 8, 10])

print(my_series)
print(my_series[1])
print(my_series[4])

# Указание индекса

my_series_step_2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

print(my_series_step_2)
print(my_series_step_2['c'])
print(my_series_step_2['a'])

# множественная выборка

print(my_series_step_2[['a', 'b', 'c']])

# групповое присваивание

my_series_step_2[['a', 'b', 'c']] = 10
print(my_series_step_2)

my_series_step_3 = pd.Series([1, 0, 2, -4, 3, 3.5, 4, 5, -7])

print(my_series_step_3[my_series_step_3 >= 3])
print(my_series_step_3[my_series_step_3 != -4])

print(my_series_step_3.values)
print(my_series_step_3.index)
print(my_series_step_3.name)

my_series_step_3.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# def task(a: list, b: list):
#     if len(a) == len(b):
#         return pd.Series(a, index=b)
#     else:
#         raise Exception('Количество значений не совпадает с количеством индексов')


# task([1, 2], [0, 1, 3])

calories = {'day_1': 300, 'day_2': 0, 'day_3': 400, 'day_4': 350,}

my_series = pd.Series(calories, index=['day_1', 'day_2', 'day_3'])

print(my_series[my_series > 0])