import numpy as np

a = np.array([1,2,3], int)
b = np.array([5,2,6], int)

print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a**b)

a = np.array([[1,2],[3,4],[5,6]], float)
b = np.array([-1,3], float)


print(a+b)

a = np.array([1,2,3,25], int)
print(np.sqrt(a))