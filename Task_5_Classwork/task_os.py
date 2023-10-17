import os

print(os.name)
print(os.environ)
print(os.getpid())
print(os.getcwd())

# os.path.exists('name_dir_new')
#
# os.mkdir('name_dir_new')
#
# os.rename('name_dir_new', 'name_dir_new_2')

import os

def create_folder(folder_name):
    """
    Создает папку с указанным именем, если она еще не существует.

    Параметры:
    folder_name (str): Название папки, которую нужно создать.

    Возвращает:
    str: Сообщение о результате операции.
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        return f'Папка "{folder_name}" успешно создана.'
    else:
        return f'Папка "{folder_name}" уже существует.'

# Пример использования функции
folder_name = "TEST"
result_message = create_folder(folder_name)
print(result_message)
