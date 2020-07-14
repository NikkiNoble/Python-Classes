class Animal:
    name = None
    weight = 0  # kg
    sound = None
    description = None

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(self.name, 'хочет есть! Надо покормить!')

    def __str__(self):
        return f'На ферме есть {self.description} по имени {self.name}, вес: {self.weight} кг, говорит: {self.sound}'


class Bird(Animal):
    eggs = 0

    def __init__(self, name, weight, eggs):
        super().__init__(name, weight)
        self.eggs = eggs

    def lay_eggs(self):
        print(f'Собрать яйца в количестве: {self.eggs}. Несушка - {self.name} {self.description}.')


class MilkGiver(Animal):

    def give_milk(self):
        print(self.name, 'нуждается в доении.')


class Cow(MilkGiver):
    sound = 'Му-у-у!'
    description = 'корова'


class Goat(MilkGiver):
    sound = 'Ме-е-е!'
    description = 'коза'


class Goose(Bird):
    sound = 'Га-га-га!'
    description = 'гусь'


class Sheep(Animal):
    sound = 'Бе-е-е!'
    description = 'овца'

    def give_fur(self):
        print(f'{self.name} нуждается в стрижке.')


class Chicken(Bird):
    sound = 'Ко-ко-ко!'
    description = 'курица'


class Duck(Bird):
    sound = 'Кря-кря!'
    description = 'утка'


def count_total_weight(list_of_animals):
    weight = 0
    for animal in list_of_animals:
        if animal.weight > weight:
            max_weight = animal.weight
            print(f'Имя самого тяжелого животного - {animal.name}, вес - {max_weight} кг.')
        weight += animal.weight
    return f'Общий вес животных - {round(weight, 2)} кг.'


cow = Cow('Манька', 670)
goose_grey = Goose('Серый', 5, 1)
goose_white = Goose('Белый', 6, 2)
goat_horns = Goat('Рога', 60)
goat_hooves = Goat('Копыта', 45)
sheep_ram = Sheep('Барашек', 70)
sheep_curly = Sheep('Кудрявый', 100)
chicken_co = Chicken('Ко-ко', 1.5, 3)
chicken_ku = Chicken('Кукареку', 2.7, 0)
duck = Duck('Кряква', 1.7, 0)

farm_animals = [
    cow, goose_grey, goose_white, goat_horns, goat_hooves, sheep_ram, sheep_curly, chicken_co, chicken_ku, duck
]
print(cow)
print(goose_grey)
print(goose_white)
print(goat_horns)
print(goat_hooves)
print(sheep_ram)
print(sheep_curly)
print(chicken_co)
print(chicken_ku)
print(duck)
goose_white.lay_eggs()
cow.give_milk()
goat_horns.feed()
sheep_curly.give_fur()
print('______________________________')
print(count_total_weight(farm_animals))