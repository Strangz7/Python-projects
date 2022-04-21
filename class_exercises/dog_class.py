class Dog:
    species = "Canis familiaris"

    # attributes
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def coat_color(self):
        return f"{self.name}'s coat is {self.color}."


class JackRussellTerrier(Dog):
    pass


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"


# buddy = Dog("Buddy", 9, "Brown")
# miles = Dog("Miles", 4, "Brown")
# print(buddy.age)
# print(miles.speak("Woff Woff"))
# print(miles.coat_color())
# print(miles)
# print(buddy)
miles = GoldenRetriever("Miles", 4, "Blue")
print(miles.speak())
