class DataBase:
    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Соединение с БД {self.user},{self.password}, {self.port} ')

    @staticmethod
    def close():
        print('закрытие соединенеия с БД')

DataBase1 = DataBase('parasha', '111', '3527')

DataBase1.connect()
DataBase1.close()


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Соединение с БД {self.user},{self.password}, {self.port} ')

    @staticmethod
    def close():
        print('закрытие соединенеия с БД')

DataBase1 = DataBase('root', '1113', 80)
DataBase2 = DataBase('root2', '5613', 40)
print(id(DataBase1), id(DataBase2))

DataBase1.connect()
DataBase2.connect()