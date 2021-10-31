class Rectangle(object):
    """Rectangle class"""
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return "Rectangle("+str(self.a)+", "+str(self.b)+")"
    def S(self):
        return self.a*self.b
    def isSquare(self):
        return self.a == self.b
    def diagonal(self):
        return (self.a**2+self.b**2)**0.5
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


