from math import hypot, cos
class Vector(object):
    """Векторний клас для лабораторної №7"""        
    def __init__(self, x = 0, y = 0):
        print("Vector({0}, {1}) initialized".format(x, y))
        self.x = x
        self.y = y    
    def __str__(self):
        return "Vector(" + str(self.x) + ", " + str(self.y) + ")"
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)    
    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)
    def length(self):
        return hypot(self.x, self.y)    
    @staticmethod
    def dotProduct(self, v):
        return self.x*v.x + self.y*v.y
    @staticmethod
    def isPerpendicular(self, v):
        return self.dotProduct(self, v) == 0

