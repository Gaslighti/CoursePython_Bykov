# 1.	Имеется строка состоящая из слов. Напишите функцию которая возвращает строку убрав из нее стоп слова. Стоп слова находятся в списке:
# a.	[“Python”, “php”, “go”, “C”]

import string
def remove_stop_words(text, stop_words):
    text = text.translate(str.maketrans('', '', string.punctuation)) # Убрали знаки препинания
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in [sw.lower() for sw in stop_words]] # поменяли регистр
    return ' '.join(filtered_words)

text = "Мой друг программирует на Python и php, но иногда использует C или go"
stop_words = ["Python", "php", "go", "C"]
new_text = remove_stop_words(text, stop_words)
print(new_text)