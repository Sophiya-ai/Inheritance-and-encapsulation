class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} can fly")

    def eat(self):
        print(f"{self.name} is eating")

    def sing(self):
        print(f"{self.name} is singing - chirik")

    def info(self):
        print(f"{self.name} - name")
        print(f"{self.voice} - voice")
        print(f"{self.color} - color")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} is singing - curlik")

    def walk(self):
        print(f"{self.name} is walking")

bird1 = Pigeon("Genry", "curlik", "grey", "bread")
bird2 = Bird("Mary", "chirik", "white")
bird1.sing()
bird1.info()
bird1.walk()
bird2.info()
bird2.sing()