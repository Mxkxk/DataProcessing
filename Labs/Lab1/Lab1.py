import math
from random import randint
import time

line = "-"
line = line*16

print("Завдання 1"+line)
x = int(input("Введіть число:"))
print(x)
print(int(x+0.8))
print(str(x)*3)

print("Завдання 2"+line)
n = int(input("Введіть кількість студентів: "))
print("Залік ", end="")
if n < 100:
	if n == 1:
		print("здав %d студент"%(n))
	elif n < 5:
		print("здало %d студенти"%(n))
	else:
		print("здало %d студентів"%(n))

print("Завдання 3"+line)
a, b = input("Введіть 2 значення: ").split()
a = float(a)
b = float(b)
print("Вхідні дані: %f %f \t Результат: %.10f"%(a, b, math.sqrt(a*b)/(math.exp(a)*b)+a*math.exp(2*a/b)))

print("Завдання 4"+line)
n, x = input("Введіть ціле і дійсне числа: ").split()
n = int(n)
x = float(x)
result = 1
for i in range(n):
	result += x**(i+1)
print("Результат: %f"%(result))

print("Завдання 5"+line)
primeDigit = int(input("Введіть просте число: "))
isDigitPrime = True
#startTime = time.time()
#for i in range(2, primeDigit):
#for i in range(2, int(primeDigit/2+1)):
for i in range(2, math.ceil(math.sqrt(primeDigit))):
	if primeDigit%i == 0:
		isDigitPrime = False
		break
#endTime = time.time();
#print("Пройшло часу: %f"%(endTime-startTime))
#час перевірки простого числа(27644437) різними методами - 21.782534 - 10.965743 - 0.004018 с
if isDigitPrime == True:
	print("%d просте число"%(primeDigit))
else: 
	print("%d не просте число"%(primeDigit))
#
print("Завдання 6"+line)
while True == True:	
	n1, n2 = randint(1, 10), randint(1, 10)	
	try:
		answer = int(input("%d x %d = "%(n1, n2)))
	except Exception:
		answer = 0		
	if answer == (n1*n2):
		break
	else: 
		print("Не правильна відповідь...")

