# prevents a user from creating an object of that class.
#  Compels a user to overrides abstaract methods in child class. 
# abstaract  class = A class which  contains one or more abstract methods.
# abstract method = A Method that has a declaration but does not have implementation.

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
  
