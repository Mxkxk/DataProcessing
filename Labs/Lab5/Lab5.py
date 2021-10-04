from random import *
import os
import re

printLine = lambda arg: print(str(arg)+"-"*50)
print("1-4")
#1
sInputedNumber = input("Введіть число:")
print("Сума цифр числа: %d"%(sum([int(i) for i in sInputedNumber])))
#2
iRandomList = [randint(0, 100) for i in range(10)]
if len(iRandomList) == len(set(iRandomList)):
	print("Всі елементи списку "+", ".join(map(str, iRandomList))+" унікальні"%(iRandomList))
else:
	print("Не всі елементи списку "+", ".join(map(str, iRandomList))+" унікальні")
#3
sText = open("text.txt", "r").read()
print("Кількість слів, що складаються з однієї букви, з файлу text: %d"%(len([s for s in sText.split() if len(s) == 1])))
#4 - голосні, що повторюються - з кириличної частини таблиці символів
print("Кількість голосних, що містяться в тексті, з файлу text: %d"%(len([s for s in list(sText) if s in "ayuioeаоуеіияюєї"])))
printLine(1.1)
#1.1
dSomeDict_old = {"some_value1":2, "some_value2":4, "some_value3":8, "some_value4":16,}
print(dSomeDict_old)
dSomeDict_new = {dSomeDict_old[k]:k for k in dSomeDict_old}
print(dSomeDict_new)
printLine(1.2)
#1.2
tStudentsSurnames = tuple(("Doe#"+str(i+1) for i in range(20)))
tRandomNumbers = tuple((randint(1, 100) for i in range(len(tStudentsSurnames))))
print(tStudentsSurnames)
print(tRandomNumbers)
printLine(1.3)
#1.3

printLine(1.4)
#1.4
sText = open("text1_4.txt", "r").read()
def function_4(sText):
	sText = re.findall("[a-z]{1,}", sText.lower())
	dWordFrequentzy = {k:1 for k in sText}
	for k in sText:
		dWordFrequentzy[k] = dWordFrequentzy[k] + 1
	for k in dWordFrequentzy:
		print("%s:%d"%(k, dWordFrequentzy[k]), end=", ")
function_4(sText)