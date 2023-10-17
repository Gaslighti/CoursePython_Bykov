import pandas as pd

my_df = pd.DataFrame({
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_1': [10234, 4325, 6728, 11874],
    'day_2': [9578, 6828, 7223, 9736],
    'day_3': [11983, 5011, 4387, 10578],
    'day_4': [8790, 6390, 5022, 12564],
})

print(my_df)

my_df = pd.DataFrame({
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_1': [10234, 4325, 6728, 11874],
    'day_2': [9578, 6828, 7223, 9736],
    'day_3': [11983, 5011, 4387, 10578],
    'day_4': [8790, 6390, 5022, 12564],
}, index=['b', 'm', 'p', 'c'])

print(my_df)

print(my_df.loc['m'])

print(my_df.loc[['b', 'm'], 'day_1'])
print(my_df.loc[['b', 'm'], ['day_1', 'day_2']])
print(my_df.loc['b': 'm'])

print(my_df.day_1)
print(my_df['day_1'])

my_df_step_2 = pd.DataFrame({
    'day_1': [10234, 4325, 6728, 11874],
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_2': [9578, 6828, 7223, 9736],
    'day_3': [11983, 5011, 4387, 10578],
    'day_4': [8790, 6390, 5022, 12564],
}).set_index('product')

print(my_df_step_2)

# my_df_step_2 = my_df_step_2.reset_index()

print(my_df_step_2)

my_df_step_2 = my_df_step_2.rename(columns={'day_1': 'day_01'})
my_df_step_2 = my_df_step_2.rename({'bread': 'bread_01'})

print(my_df_step_2)

my_df_step_2['sum'] = my_df_step_2.sum(axis=1)
print(my_df_step_2)

my_df_step_2 = my_df_step_2.drop(['day_4'], axis='columns')
my_df_step_2 = my_df_step_2.drop('candies')

print(my_df_step_2)

flights = pd.DataFrame({
    'id': [0, 1, 2, 3],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 9, 3, 1],
    'dep_time': [517.0, 533.0, 542.0, 544.0],
    'sched_dep_time': [515, 529, 540, 545],
}).set_index('id')

print(flights[flights.month == 1])

flights['diff'] = flights['dep_time'] - flights['sched_dep_time']
print(flights)