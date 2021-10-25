class Student(object):
    """Student class for lab 8"""
    def __init__(self, surname):
        self.surname = surname
        self.__zalik = None    
    @property
    def zalik(self):
        if self.__zalik == True:
            return "Зарах"
        else:
            return "Не зарах"
    @zalik.setter
    def zalik(self, z):
        self.__zalik = z    

