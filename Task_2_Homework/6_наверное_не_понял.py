# 6.	Напишите декоратор который выводит исключение в случае если декорируемая функция
# возвращает тип данных отличный от int.
# Напишите 2 тестовые декорируемые функции с произвольными данными.


# Не думаю, что правильно понял суть задания

def enforce_int_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)


        if all(map(lambda x: isinstance(x, int), [result])):
            return print(result)
        else:
            print(TypeError("Значение должно быть типа int."))

    return wrapper


# Test functions
@enforce_int_return_type
def test_func_1(x):
    return x*3


test_func_1(2)

@enforce_int_return_type
def test_func_2(x):
    return x*3

test_func_2('sttt')