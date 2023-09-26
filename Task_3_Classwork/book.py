class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print('Book on abonent')
        else:
            self.checked_out = True
            print("Give book to abonent")

    def check_in(self):
        if not self.checked_out:
            print('Book have')
        else:
            self.checked_out = False
            print('Take book in libraury')

book1 = Book('Война и Мир', ' В.Н.Толстой')

book1.check_out()
book1.check_out()

book1.check_in()
book1.check_in()