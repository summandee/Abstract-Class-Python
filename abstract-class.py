# prevents a user from creating an object of that class
#  Compels a user to overrides abstaract methods in child class 

from abc import ABC,  abstractmethod
class Vehicle:
  def go(self):
    pass

class Car(Vehicle):
  def go(self):
    print("You Drive the Car")

class Motorcycle(Vehicle):
  def go(self):
    print("You ride the Motorcycle")

# These Are objects
vehicale = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicale.go()
car.go()
motorcycle.go()
  
