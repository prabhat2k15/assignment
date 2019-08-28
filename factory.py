from __future__ import generators
import random

class Shape(object):

    @staticmethod
    def factory(type):
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        assert 0, "Bad shape creation: " + type
    

class Circle(Shape):
    def area(self, radius):
        print('Area of circle: {}'.format(3.414 * (radius*radius)))

class Square(Shape):
    def area(self, side):
        print('Area of square: {}'.format(side*side))

# s= Shape.factory('Square')
# s.area(5)

# s= Shape.factory('Circle')
# s.area(5)