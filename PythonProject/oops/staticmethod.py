class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    @staticmethod
    def create_animal(name, animal_type):
        if animal_type == 'dog':
            return Dog(name)
        elif animal_type == 'cat':
            return Cat(name)
        else:
            raise ValueError('Invalid animal type')


class Dog(Animal):
    def speak(self):
        return 'Woof!'


class Cat(Animal):
    def speak(self):
        return 'Meow!'

class Car:
    _count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car._count += 1

    @staticmethod
    def count():
        return Car._count

# This demonstrates how class-level state can be used in a
# static method to keep track of information across all instances of the class.
#
# This can be useful in scenarios where you want to keep track of how many
# instances of a class have been created or to implement class-level caching or memoization of expensive computations or operations.


# Create a dog and a cat
my_dog = Animal.create_animal(name='Loby', animal_type='dog')  # Create an animal of type dog
my_cat = Animal.create_animal(name='Garfield', animal_type='cat')  # Create an animal of type cat
random = Animal.create_animal(name='Random', animal_type='random')  # ValueError: Invalid animal type

print(my_dog.speak())  # Woof!
print(my_cat.speak())  # Meow!
#note here static method is used as a factory method