class Car:



    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def color(self):
        return f"The {self.color} car has {self.mileage} miles."

    def drive(self, move):
        miles = self.mileage + move
        return miles


camry = Car("Yellow", 100)
# benz = Car("Red", 30000)
# print(Car.color(camry))
# print(Car.color(benz))
print(camry.drive(100))
