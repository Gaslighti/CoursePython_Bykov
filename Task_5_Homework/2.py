# 2.	В DataFrame из предыдущего задания добавьте индексы строк в виде латинских букв. Выведите на печать строку в которой все числа > 5, если такая есть

import pandas as pd
import numpy as np
import random
import string

# Устанавливаем seed для воспроизводимости результатов
random.seed(42)

# Генерируем DataFrame с рандомными целыми числами от 1 до 10 размером 10x10
data = np.random.randint(1, 11, size=(10, 10))
df = pd.DataFrame(data, columns=[f'col{i+1}' for i in range(10)])

# Генерируем индексы строк в виде латинских букв
index_labels = [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(10)]
df.index = index_labels

# Выводим DataFrame
print("DataFrame с индексами в виде латинских букв:")
print(df)

# Выводим строку, где все числа больше 5
# Если такой строки нет, выводим сообщение
found_row = df[(df > 5).all(axis=1)]
if not found_row.empty:
    print("\nСтрока, где все числа больше 5:")
    print(found_row)
else:
    print("\nВ DataFrame нет строки, где все числа больше 5.")
