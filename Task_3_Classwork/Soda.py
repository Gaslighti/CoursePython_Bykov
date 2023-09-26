class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'soda and {self.ing}')

        else:
            print('common soda')


drink1 = Soda()
drink2 = Soda('bredberry')
drink1.show_my_drink()
drink2.show_my_drink()