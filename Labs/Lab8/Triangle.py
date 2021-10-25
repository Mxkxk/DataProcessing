from math import sqrt
class Triangle(object):
    """Triangle class for lab 8"""
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c
    def P(self):
        return self.a+self.b+self.c
    def S(self):
        p = self.P()/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
class RightTriangle(Triangle):
    """Right Triangle class for lab 8"""
    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b
        self.c = sqrt(side_a**2 + side_b**2)
    def S(self):
        return self.a*self.b/2
class EquilateralTriangle(Triangle):
    """Equilateral Triangle class for lab 8"""
    def __init__(self, side_a):
        self.a = side_a
        self.b = side_a
        self.c = side_a
    def S(self):
        return self.a**2*sqrt(3)/4
