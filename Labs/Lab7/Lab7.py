from Vector import *
from Student import *
from IterableClass import *
# vcVariable -> vector variable

#Завдання 1-----------------------------------------
print("Task 1" + "-"*40)
vcList = [Vector(i, i**2) for i in range(5)]
print(Vector(1, 0) == Vector(1, 0))
vSum = Vector(1, 4) + Vector(3, 10)
print("Previous vector length: " + str(vSum.length()))
print("Dot product of 2 previos vectors: " + str(Vector.dotProduct(Vector(2, 2), Vector(2, 0))))
print("Are vectors colinear? " + str(Vector.isPerpendicular(Vector(2, 0), Vector(1, 3))))
print("Are vectors colinear? " + str(Vector.isPerpendicular(Vector(0, 4), Vector(4.7, 0))))
#Завдання 2-----------------------------------------
print("Task 2" + "-"*40)
stud = Student("John", "Doe", {"Calculus":[4, 5, 4, 5, 4, 3], "Linear geometry":[5, 3, 3, 5, 4, 2], "C++":[4, 4, 4, 3]})
print(stud)
print(stud.getAllSubjects())
print("Calculus:" + str(stud.getMarksForSubject("Calculus")))
print("Calculus middle valued mark: %.2f"%(stud.getMidValuedMarkForSubject("Calculus")))
stud.addMarkToSubject("Calculus", 1)
print("Calculus:" + str(stud.getMarksForSubject("Calculus")))
print("Student passed calculus? {0}".format(stud.passedSubject("Calculus")))
print("Calculus middle valued mark:%.2f"%(stud.getMidValuedMarkForSubject("Calculus")))
print("Linear geometry middle valued mark:%.2f"%(stud.getMidValuedMarkForSubject("Linear geometry")))
print("Python:"+stud.getMidValuedMarkForSubject("Python"))
stud.addSubject("Python", [5, 5, 5, 4])
print(stud.getAllSubjects())
print("Python:" + str(stud.getMarksForSubject("Python")))
print("Middle valued mark of all subjects:%.2f"%(stud.getMidValuedMarkForAllSubjects()))
stud.showAllMidValuedMarks()
#Завдання 3-----------------------------------------
def showIter(iter_):
	while True:
		try:
			print(next(iter_))
		except Exception:
			break
print("Task 3" + "-"*40)
iterIter = iter(IterableClass(0, 20, 3))
showIter(iterIter)
print("*"*10)
iterIter = iter(IterableClass(30, -20, -2))
showIter(iterIter)