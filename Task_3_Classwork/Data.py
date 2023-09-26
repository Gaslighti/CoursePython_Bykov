class Data:
    def __new__(cls, *args, **kwargs):
        print('state fetching')
        return super().__new__(cls)

    def __init__(self, my_list):
        self.my_list = my_list
        print(f'data processing: {self.my_list}')


obj = Data([1,2,3,4])
obj2 = Data(['a','b', 'c','d'])