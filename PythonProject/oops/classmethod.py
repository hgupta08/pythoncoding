class ThreeDPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi. I'm {self.first_name} {self.last_name}. I'm {self.age} years old."

   #
   # When a method creates an instance of class
   #  class and returns it, the method is called a factory method.
   #  For example, the create_anonymous() is a factory method because it
   #  returns a new instance of the Person class.


    #note it takes class as a paramerter
    @classmethod
    def create_anonymous(cls):
        return Person('John', 'Doe', 25)


if __name__=="__main__":

    anonymous = Person.create_anonymous()
    print(anonymous.introduce())


    ThreeDPoint.from_sequence((4, 8, 16))

    point = ThreeDPoint(7, 14, 21)
    point.from_sequence((3, 6, 9))