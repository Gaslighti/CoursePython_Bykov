# Необходимо создать классовую структуру по описанию
# допонить задачу 4

import random


class Apple:
    STAGES_OF_RIPENING = ['цветение', 'зеленое', 'красное']

    def __init__(self, index):
        self.index = index
        self.ripening_stage = self.STAGES_OF_RIPENING[0]
        self.age_without_harvest = 0  # Счетчик для отслеживания несобранных яблок

    def ripen(self):
        current_stage_index = self.STAGES_OF_RIPENING.index(self.ripening_stage)
        if current_stage_index < len(self.STAGES_OF_RIPENING) - 1:
            self.ripening_stage = self.STAGES_OF_RIPENING[current_stage_index + 1]

    def is_ripe(self):
        return self.ripening_stage == self.STAGES_OF_RIPENING[-1]

    def increment_age_without_harvest(self):
        self.age_without_harvest += 1

    def is_overripe(self):
        return self.age_without_harvest >= 3


class Tree:
    def __init__(self,  *apples, age):
        self.apples = []
        if age < 2:
            if len(apples) > 0:
                print("Warning: Tree age contradicts the condition of having apples. Age should be 2 or greater.")
        else:
            if len(apples) > 0:
                self.apples = list(apples)
        self.age = age

    def grow(self):
        self.age += 1

        if self.age >= 2 and self.age <= 4:
            # Randomly decide if a new apple appears during growth
            new_apple_count = random.randint(10, 100)
            for i in range(new_apple_count):
                new_apple = Apple(len(self.apples) + 1)
                new_apple.ripening_stage = 'цветение'  # New apples should start at the 'цветение' stage
                self.apples.append(new_apple)

        # Update apple ripening stages
        for apple in self.apples:
            apple.ripen()

        # Remove apples if they are overripe
        for apple in self.apples:
            apple.increment_age_without_harvest()
        self.apples = [apple for apple in self.apples if not apple.is_overripe()]

        # Remove apples if the tree is too old
        if self.age >= 10:
            self.apples = []


class Gardener:
    def __init__(self, name, *plants):
        self.name = name
        self.plants = list(plants)
        self.total_harvested_apples = 0  # Счетчик для общего количества собранных яблок

    def take_care_of_plants(self):
        for plant in self.plants:
            plant.grow()

    def harvest(self):
        ripe_apples = []
        for plant in self.plants:
            if isinstance(plant, Tree):
                for apple in plant.apples:
                    if apple.is_ripe():
                        ripe_apples.append(apple)
                        self.total_harvested_apples += 1
        return ripe_apples

    def garden_statistics(self):
        tree_count = sum(1 for plant in self.plants if isinstance(plant, Tree))
        tree_ages = [plant.age for plant in self.plants if isinstance(plant, Tree)]
        apple_count_by_stage = {stage: sum(
            1 for plant in self.plants if isinstance(plant, Tree) for apple in plant.apples if
            apple.ripening_stage == stage) for stage in Apple.STAGES_OF_RIPENING}

        return {
            'tree_count': tree_count,
            'tree_ages': tree_ages,
            'apple_count_by_stage': apple_count_by_stage,
            'total_harvested_apples': self.total_harvested_apples
        }


# Testing the classes
if __name__ == "__main__":
    # Create 5 apples
    apples = [Apple(i) for i in range(1, 6)]

    # Create a tree with the apples and an initial age of 2
    tree = Tree( *apples, age=2)

    # Create a gardener and add the tree to the garden
    gardener = Gardener('John', tree)

    # Display initial garden statistics
    print("Initial garden statistics:")
    print(gardener.garden_statistics())

    # Simulate 10 cycles of care and growth
    for cycle in range(10):
        print(f"\nCycle {cycle + 1}")
        gardener.take_care_of_plants()
        ripe_apples = gardener.harvest()
        if ripe_apples:
            print(f"Harvested {len(ripe_apples)} apples.")
        else:
            print("No apples were harvested.")

        # Display garden statistics after each cycle
        print("Garden statistics:")
        print(gardener.garden_statistics())


