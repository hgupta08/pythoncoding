# Validating input is one of the most common use cases of property() and
# managed attributes. Data validation is a common requirement in code that
# takes input from users or other sources that you could consider untrusted.
# Python’s property() provides a quick and reliable tool for dealing with input validation.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None



point = Point(12, 5)

print(point.x)
print(point.y)


point.x = 42


point.y = 100.0

print(point.x)
print(point.y)
point.x = "one"

point.y = "1o"

print(point.x)
print(point.y)