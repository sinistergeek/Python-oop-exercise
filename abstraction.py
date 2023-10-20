from abc import ABC

class Vechicle(ABC):

    def no_of_wheels(self):
        pass

class Cycle(Vechicle):
    def no_of_wheels(self):
        print("Cycle have 2 wheels")

class Car(Vechicle):
    def no_of_wheels(self):
        print("Car have 4 wheels")

class HeavyTruck(Vechicle):
    def no_of_wheels(self):
        print("HeavyTruck have 8 wheels")

Cycle =Cycle()
Cycle.no_of_wheels()
Car = Car()
Car.no_of_wheels()
HeavyTruck = HeavyTruck()
HeavyTruck.no_of_wheels()
