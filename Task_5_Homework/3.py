# 3.	Создайте DataFrame с рандомными числами, размером 10х10.
# a.	добавьте индексы столбцов и строк в виде латинских букв
# b.	Выведите на в консоль
# i.	Размерность матрицы
# ii.	индексы столбцов
# iii.	среднее значение всех чисел матрицы
# iv.	запишите матрицу в csv

import pandas as pd
import numpy as np
import random
import string

# Генерируем DataFrame с рандомными числами от 1 до 100 размером 10x10
data = np.random.randint(1, 101, size=(10, 10))

# Генерируем индексы строк и столбцов в виде латинских букв
index_labels = [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(10)]
column_labels = [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(10)]

# Создаем DataFrame с индексами и столбцами
df = pd.DataFrame(data, index=index_labels, columns=column_labels)

# Выводим размерность матрицы
print("Размерность матрицы:", df.shape)

# Выводим индексы столбцов
print("Индексы столбцов:", df.columns.tolist())

# Выводим среднее значение всех чисел в матрице
mean_value = df.values.mean()
print("Среднее значение всех чисел матрицы:", mean_value)

# Записываем матрицу в CSV
csv_filename = "matrix.csv"
df.to_csv(csv_filename)

# Выводим сообщение о сохранении в файл
print("Матрица сохранена в файл:", csv_filename)
