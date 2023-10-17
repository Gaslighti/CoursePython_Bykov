import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

flights = pd.DataFrame({
    'id': [0, 1, 2, 3],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 9, 3, 1],
    'dep_time': [517.0, 533.0, 542.0, 544.0],
    'sched_dep_time': [515, 529, 540, 545],
}).set_index('id')

print(flights)
plt.plot(flights.groupby('month')['dep_time'].sum())
plt.savefig('flights.png')
