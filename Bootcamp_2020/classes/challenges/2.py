"""
Question 2
Create a circle class that will take the value  of radius and return the area of a circle.
"""
from math import pow, pi


class Circle(object):
    """
        Attributes
        ----------
        radius : represents a line segment from circle center to its perimeter
    """

    def __init__(self, radius=1):
        self.radius = radius

    def calc_area(self):
        area = pi * pow(self.radius, 2)
        return f'{area:.2f}'


my_circle = Circle(15)
print(my_circle.calc_area())
