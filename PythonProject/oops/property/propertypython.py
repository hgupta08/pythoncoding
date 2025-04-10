# Note: Getter and setter methods are often considered an anti-pattern and
# a signal of poor object-oriented design.
# The main argument behind this proposition is that these methods break encapsulation.
# They allow you to access and mutate the components of your objects from the outside.
from pprint import pprint


class Pythonicwayclass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# This code uncovers a fundamental Python principle: exposing
# attributes to the end user is normal and common.
# This is cool because you don’t need to clutter
# your classes with getter and setter methods all the time.
#
# To define a getter and setter method while
#     achieving backward compatibility, you can use the property() class.
class Personwithoutproperty:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)

if __name__=="__main__":
    print(Person.age)

    john = Person('John', 18)
    pprint(john.__dict__)

    john.age = 19
    print(Person.age)

    pprint(Person.__dict__)
    point = Point(12, 5)
     # Non-public attributes are still accessible

    print(point._x)
    p=Person("name",2)
    print(p.age)
# _x. From the two final examples, you can confirm that Python doesn’t restrict access to
# non-public attributes.
# Whether or not you access them directly is up to you.



