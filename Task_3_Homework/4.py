# Необходимо создать классовую структуру по описанию
# a.	Имеется яблоко со следующими характеристиками:

class Apple:
    STAGES_OF_RIPENING = ['цветение', 'зеленое', 'красное']

    def __init__(self, index):
        self.index = index
        self.ripeness_stage = self.STAGES_OF_RIPENING[0]

    def ripen(self):
        if self.ripeness_stage == self.STAGES_OF_RIPENING[-1]:
            return False
        current_stage_index = self.STAGES_OF_RIPENING.index(self.ripeness_stage)
        self.ripeness_stage = self.STAGES_OF_RIPENING[current_stage_index + 1]
        return True

    def is_ripe(self):
        return self.ripeness_stage == self.STAGES_OF_RIPENING[-1]

class Tree:
    def __init__(self, *apples):
        self.apples = list(apples)

    def grow(self):
        for apple in self.apples:
            apple.ripen()

    def all_apples_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def harvest(self):
        if self.all_apples_ripe():
            self.apples = []
            return True
        else:
            print(f"Не все яблоки на дереве созрели.")
            return False

class Gardener:
    def __init__(self, name, *trees):
        self.name = name
        self.trees = list(trees)

    def take_care_of_plants(self):
        for tree in self.trees:
            tree.grow()

    def harvest_all(self):
        while not all(tree.harvest() for tree in self.trees):
            self.take_care_of_plants()
            print("Информация о зрелости яблок:")
            for apple in apples:
                print(f"Яблоко {apple.index}: {apple.ripeness_stage}, зрелость: {apple.is_ripe()}")

        print("Урожай собран.")


# Тестирование
# Создаем 5 яблок
apples = [Apple(i) for i in range(1, 6)]

# Создаем дерево с этими яблоками
tree = Tree(*apples)

# Создаем садовника, который следит за деревом
gardener = Gardener("Иван", tree)

# Проводим уход за растениями, проверку зрелости яблок и сбор урожая
gardener.harvest_all()