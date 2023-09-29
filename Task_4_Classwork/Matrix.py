import numpy as np

a = np.array([[1,2,3],[4,5,6]], float)

print(a[0,1])
print(a[1,1])

print(a.shape)
print(a.dtype)

b = np.array(range(10), float)
b_reshape = b.reshape((2,5))

print(b)
print(b_reshape)

print(b.tolist())

def task(*args):
    my_list = sorted(list(filter(lambda x: type(x) == int, list(args))))
    return np.array(my_list, int)


print(task('1',2,3.3333,1,10,'pwd','ls - la'))

def task_2(x,y):
    result=np.random.random((x,y))
    return result.mean(),result.min(),result.max()


print(task_2(5,10))