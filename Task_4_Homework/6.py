# 6.	Постройте класс для анализа файла с данными:
# a.	Класс принимает путь к файлу при инициализации
# b.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
# Файл состоит из строк с произвольным текстом, элементами массива должны быть строки.
# c.	Создайте метод поиска по тексту. Метод принимает паттерн поиска и возвращает список всех найденных совпадений.

import re


class FileAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []  # Список для хранения данных из файла

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                # Чтение данных из файла и сохранение в атрибут класса
                self.data = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Файл не найден.")

    def search_by_pattern(self, pattern):
        matches = []
        for line in self.data:
            # Поиск совпадений по паттерну и добавление их в список
            found_matches = re.findall(pattern, line)
            matches.extend(found_matches)
        return matches


# Пример использования
file_path = 'example.txt'  # Путь к файлу с данными
analyzer = FileAnalyzer(file_path)

# Чтение файла
analyzer.read_file()

# Паттерн для поиска
search_pattern = r'\b\w+\b'  # Паттерн для поиска слов

# Поиск по тексту и вывод результатов
matches = analyzer.search_by_pattern(search_pattern)
print("Найденные совпадения:")
print(matches)
