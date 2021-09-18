import random

#sInputedComand - ввделена послідовність команд

vLineSpacer = lambda sSpacerText: print('-' * 10 + str(sSpacerText) + '-' * 10 )

while True == True:
	sInputedComand = input('Виберіть пункт меню: ')
	try:
		sInputedComand = int(sInputedComand)
	except Exception:
		sInputedComand = 0

	if sInputedComand == 1:
		continue
	elif sInputedComand == 2:
		continue
	elif sInputedComand == 3:
		continue
	elif sInputedComand == 4:
		continue
	elif sInputedComand == 5:
		continue
	elif sInputedComand == 6:
		print("Завершення роботи...")
		break
	else:
		print("Ви ввели не правильну команду")	

