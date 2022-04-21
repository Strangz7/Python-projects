class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I speak"


class Dog(Animal):
    def __init__(self, name, type_):
        super().__init__(name)
        self.type = type_

    def speak(self):
        super().speak()
        return "Dog speak"


class Cat(Animal):
    pass

dog = Dog("Bingo", "y")
print(dog)