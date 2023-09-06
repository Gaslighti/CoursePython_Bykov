# 7.	Напишите декоратор который запускает декорируемую функцию повторно, в случае если произошло исключение при первом запуске.
# Напишите 2 тестовые декорируемые функции с произвольными данными.




#Вот декоратор, который работает дважды с функцией
def retry_on_exception(func):
    def wrapper(*args, **kwargs):
        attempts = 2
        for _ in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if _ == attempts - 1:
                    raise e

    return wrapper




@retry_on_exception
def test_func(x):
    import random
    number = random.randint(0,x)  # это должно быть рандмное число
    x=x-number
    if x == 0: #если введенное число минус рандомное равно 0 то выскакивает ошибка
         print(ValueError("Ошибка"))
    return print(x)


test_func(3) # Работает так в 1 раз выводится ошибка, во второй значение, которое получается.
# Дожно работать так: если введеное число минус рандомное число = 0, то ошибка, и запускается вновь с новым рандомным числом.

test_func(10)