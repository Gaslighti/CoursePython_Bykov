#8)	Напишите функцию которая
#a)	на вход получает строковую переменную.
#i)	в строке содержится несколько слов
#b)	Возвращает строку состоящую из аббревиатур слов переменной.
#c)	Если на вход поступил другой тип данных, должно срабатывать исключение
#d)	Результат работы функции распечатайте в консоль

input_str1 = 'string school ETC'
input_str2 = 12

def abbreviate_words(input_str):
    if isinstance(input_str,str):
        words = input_str.split()
        abbreviations = [word[0].upper() for word in words]
        result = ''.join(abbreviations)
        return result
    else:
        return "Переменная должна быть строкой"




print(abbreviate_words(input_str1))
print(abbreviate_words(input_str2))


