class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."


if __name__=="__main__":
    john = Person("John Doe", 35)

    print( repr(john))
    print( str(john))

# The .__repr__() method gives you a developer-friendly string representation of specific Person
# objects. You’ll be able to re-create the object using the output of the repr() function.
# In contrast, the string representation that you get from calling .__str__() should aim to
# be readable and informative for end users. You can access this representation with the str()
# function.



