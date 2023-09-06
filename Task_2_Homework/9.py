# 9.	* Напишите декоратор который измеряет время выполнения декорируемой функции.

import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):

        if not hasattr(wrapper, "Timex"):
            wrapper.Timex = 0


        if wrapper.Timex == 0:
            wrapper._start_time = time.time()

        wrapper.Timex += 1
        result = func(*args, **kwargs)
        wrapper.Timex -= 1

        if wrapper.Timex == 0:
            end_time = time.time()
            elapsed_time = end_time - wrapper._start_time
            print(f"Функция {func.__name__} рассчитывалась {elapsed_time:.6f} секунд.")

        return result

    return wrapper

@timer_decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci( n -1) + fibonacci( n -2)

# Testing the decorator with fibonacci function
print(fibonacci(30))

@timer_decorator
def function_2(x):
    return x**x


print(function_2(21))




