class Student(object):
    """Студентський клас для лабораторної 7"""
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
    def __str__(self):
        return self.name + " " + self.surname;
    def getAllSubjects(self):
        return "Subjects:\n\t"+"\n\t".join(map(str, self.marks.keys()))
    def getMarksForSubject(self, subject):
        return self.marks[subject]
    def getMidValuedMarkForSubject(self, subject):
        if self.marks.__contains__(subject):
            return sum(self.marks[subject])/len(self.marks[subject])
        else:
            return "This subject doesn`t exist"
    def getMidValuedMarkForAllSubjects(self):
        return sum([self.getMidValuedMarkForSubject(i) for i in self.marks])/len(self.marks)
    def addSubject(self, subject, marks):
        self.marks[subject] = marks
    def passedSubject(self, subject):
        return self.getMidValuedMarkForSubject(subject) > 4
    def addMarkToSubject(self, subject, mark):        
        self.marks[subject].append(mark)
    def showAllMidValuedMarks(self):
        ret = str(self)+"`s middle valued marks from subjects:"
        for k in self.marks:
            ret+= "\n\t" + k + ":" + str(self.getMidValuedMarkForSubject(k))
        print(ret)