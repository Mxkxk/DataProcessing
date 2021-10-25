from Triangle import *
from CurrencyTrading import *
from Student import *

#1
triangle = Triangle(3, 4, 5)
print("Площа трикутника:"+str(triangle.S()))
rTriangle = RightTriangle(3, 4)
print("Площа прямокутного трикутника:"+str(rTriangle.S()))
eTriangle = EquilateralTriangle(4)
print("Площа прямокутного трикутника:"+str(eTriangle.S()))

#2
currency = CurrencyTrading()
print(currency.trade("USD", "EUR", 1))
print(currency.trade("USD", "UAH", 1))
print(currency.trade("UAH", "USD", currency.trade("USD", "UAH", 1)[1]))
print(currency.trade("UAH", "UAH", 1))
print(currency.trade("UAH", "RUB", -20))
print(currency.trade("UAH", "EUR", 28))

#3
student = Student("John Doe")
student.zalik = True
print(student.surname + " має: " + student.zalik)
student = Student("Jane Doe")
student.zalik = "nope"
print(student.surname + " має: " + student.zalik)