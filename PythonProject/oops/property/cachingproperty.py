import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius must be positive')

        if value != self._radius:
            self._radius = value
            self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius ** 2

        return self._area

#here we are using caching ...we are not calling the area again and again
#we have sent it to None once we change it we will call it
#Second, if the radius changes, reset the area. Otherwise,
# return the area directly from the cache without recalcuation.