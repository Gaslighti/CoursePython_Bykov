#5)	Напишите функцию которая отвечает “ДА” или “НЕТ” на вопрос в комментарие.
#str_2 содержит в себе str_1

str_1='test'
str_2='test1'



def Answer(str_1,str_2):
    number_str1=len(str_1)
    proverka=str_2[0:number_str1]
    proverka_2=str_1
    if proverka == proverka_2:
        print('ДА')
    else:
        print('No')

Answer(str_1,str_2)
