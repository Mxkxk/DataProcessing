from Rectangle import *
import datetime

discretion = lambda n: print(str(n)+"-"*50)
#1
discretion("#1")
def delMiddleDigit(digit):
	digit = str(digit)
	if len(digit)%2 == 0:
		return "Число парне(("
	else:		
		digit = [digit[s] for s in range(len(digit)) if s!= int(len(digit)/2)]
		digit = int("".join(digit))
		return digit

digit = 10245976120
print(digit, delMiddleDigit(digit))
digit = 1024596120
print(digit, delMiddleDigit(digit))

#2
discretion("#2")
vec = [{"surname":"Surname", "gender":"m", "birthDate": "3.10.1992"},
	   {"surname":"Doe", "gender":"f", "birthDate": "17.05.1999"},
	   {"surname":"Pupkin", "gender":"m", "birthDate": "1.06.1985"},
	   {"surname":"Dody", "gender":"m", "birthDate": "19.09.1977"},
	   {"surname":"Grenda", "gender":"f", "birthDate": "19.09.1972"}]
def findOldestEmployee(vec):
	dates = ["-".join(str(d["birthDate"]).split(".")[::-1]) for d in vec if d["gender"] == "m"]
	surs = [d["surname"] for d in vec if d["gender"] == "m"]
	return surs[dates.index(min(dates))]
def findByFirstSurnameSymbol(vec, s):
	employees = []
	for employee in vec:
		if employee["surname"].lower()[0] == s.lower():
			employees.append(employee)
	return employees

print(findOldestEmployee(vec))
print(findByFirstSurnameSymbol(vec, "d"))
#3
discretion("#3")
def AlwaysAboveZero(func):
	def AAZ(*func_args):
		ret = func(*func_args)
		if ret < 0:
			return func(*func_args)*(-1)
		elif ret == 0:
			return 1
	return AAZ

sumAAZ = AlwaysAboveZero(sum)
l = [1, -10, 4]
print("Сума більша за 0 списка "+ str(l)+ ": " + str(sumAAZ(l)))

#4
discretion("#4")
rect = Rectangle(3, 6)
print(rect)
print("Rect square is "+str(rect.S()))
print("Is rect square? - "+str(rect.isSquare()))
print("Rect diagonal is "+str(rect.diagonal()))
print("Is " + str(rect) + " equal to " + str(Rectangle(4, 2)) + "? - " + str(rect == Rectangle(4,2)))