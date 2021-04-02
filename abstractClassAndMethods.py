from abc import *


# An abstract method is a method which only has declaration and doesn't have definition.
# A class is called abstract class only if it has at least one abstract method.


class Person(ABC):
    @abstractmethod
    def name(self):
        pass


class Employee(Person):
    def name(self):
        print("Hello I am Jhon!")


e = Employee()
e.name()
