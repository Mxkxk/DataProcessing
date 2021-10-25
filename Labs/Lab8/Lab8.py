from Triangle import *
from CurrencyTrading import *
#1
triangle = Triangle(3, 4, 5)
print("Площа трикутника:"+str(triangle.S()))
rTriangle = RightTriangle(3, 4)
print("Площа прямокутного трикутника:"+str(rTriangle.S()))
eTriangle = EquilateralTriangle(4)
print("Площа прямокутного трикутника:"+str(eTriangle.S()))

#2
currency = CurrencyTrading()
print(currency.trade("USD", "UAH", 1000))
