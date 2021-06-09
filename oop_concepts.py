"""
    Concept of inheritance
"""


class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"{self.name} has {self.mileage} km/l mileage."


class BMW(Car):
    pass


class Audi(Car):
    
    def description(self):
        # super().description()
        return f"{self.name} can run {self.mileage} for per litre."


obj1 = BMW('Seies-7', 30.22)
print(obj1.description())
obj2 = Audi('Q-7', 20)
print(obj2.description())


"""
    Concept of encapsulation
"""


class Bird1:
    def __init__(self, name, colour):
        self._name = name   # protected member
        self.colour = colour

    def description(self):
        return f"{self._name} has {self.colour} colour."


class Parrot1(Bird1):
    pass


obj3 = Parrot1('Maverick', 'Black')
print(obj3.description())
print(obj3._name)   # "_" (_name) defines protected attribute
print(obj3.colour)


class Bird2:
    def __init__(self, name, colour):
        self.__name = name   # private member
        self.colour = colour

    def description(self):
        return f"{self.__name} has {self.colour} colour."


class Parrot2(Bird2):
    pass


obj4 = Parrot2('Sir the grey', 'Grey')
print(obj4.description())
# Following line gives error because "__" (__name) defines private attribute
# print(obj4.__name)


"""
    Polymorphism
"""


class Football:
    def game_description(self):
        print("This class defines description of Football")


class Baseball:
    def game_description(self):
        print("This class defines description of Baseball")


football = Football()
baseball = Baseball()
for game in (football, baseball):
    game.game_description()

