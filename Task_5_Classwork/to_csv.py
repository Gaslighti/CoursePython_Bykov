import pandas as pd

flights = pd.DataFrame({
    'id': [0, 1, 2, 3],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 9, 3, 1],
    'dep_time': [517.0, 533.0, 542.0, 544.0],
    'sched_dep_time': [515, 529, 540, 545],
}).set_index('id')

flights.to_csv('flights.csv')