import random
import os

vClearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
vLineSpacer = lambda sSpacerText: print('-' * 10 + str(sSpacerText) + '-' * 10 )
fsHelp = open("help.txt", "r")
sHelp = fsHelp.read()
fsHelp.close()
iTask = 0
iAmmounOfTasks = lambda : 5

Dictionary = {}
Dictionary["Berlin"] = "Germany"
Dictionary["Kyiv"] = "Ukraine"
Dictionary["Warsaw"] = "Poland"
Dictionary["Tokio"] = "Japan"
Dictionary["Paris"] = "France"

while True == True:
### Вибір завдання
	sChangeTask = input("Виберіть завдання:")
	sChangeTask = str.lower(sChangeTask)
	if sChangeTask == "h" or sChangeTask == "help":
		print(sHelp)
	elif sChangeTask == "end" or sChangeTask == "close" or sChangeTask == "n":		
		break
	elif sChangeTask == "clear" or sChangeTask == "clr":
		vClearConsole()
	else:
		try:
			iTask = int(sChangeTask)
			if iTask < 1 or iTask > iAmmounOfTasks():
				print("Ви увели завдання, якого не існує, спробуйте ще раз. Можете скористатися командою help або h")
		except Exception:
			print("Ви увели щось не правильно, спробуйте ще раз. Можете скористатися командою help або h")					
### Перше завдання
	if iTask == 1:
		vLineSpacer("Перше завдання")
		lFirstTask = []
		iLen = 0
		try:
			iLen = int(input("Введіть довжину списку: "))
		except Exception:
			print("Число не вірно вказане...")
		for i in range(iLen):
			lFirstTask.append(input("Введіть %d значення в списку: "%(i+1)))		
		if len(lFirstTask) > 0:
			print(lFirstTask)
			print("Довжина списку: %d"%(len(lFirstTask)))
			del lFirstTask[0]
		### 1.2
			iLen = 0
			try:	
				iLen = int(input("Введіть довжину списку випадкових значень: "))
			except Exception:
				print("Число не вірно вказане...")
			lRandList = []
			if iLen > 0:
				for i in range(iLen):
					lRandList.append(random.randint(1, 10))				
				lFirstTask.extend(lRandList)
				print(lFirstTask)
		del lFirstTask
		vLineSpacer("Кінець першого завдання")
### Друге завдання
	elif iTask == 2:
		vLineSpacer("Друге завдання")
		sWord = input("Введіть слово: ")
		lWord = list(sWord)
		print(lWord)
		vLineSpacer("Кінець другого завдання")
### Третє завдання
	elif iTask == 3:
		vLineSpacer("Третє завдання")
		iDivisor = None
		try:
			iDivisor = float(input("Введіть дільник: "))
		except Exception:
			print("Число не вірно вказане")
		try:
			iDivisor = 1/iDivisor
		except ZeroDivisionError:
			print("Ділити на нуль не можна")
		vLineSpacer("Кінець третього завдання")
## Основне завдання
	elif iTask == 4:
		#sInputedComand - ввделена послідовність команд
		vLineSpacer("Основне завдання")		
		List = []
		isCreatedList = False
		#константа кількості пунктів меню
		iAmmounOfTasksTask4 = lambda : 6

		while True == True:
			###виведення меню і отримання команди
			lMenu = ["My menu", "\t1:create list", "\t2:add element", "\t3:preview", "\t4:exit", "\t5:create list of natural numbers"]
			for i in lMenu:
				print(i)			
			sInputedComand = input('$:')
			###
			try:
				sInputedComand = int(sInputedComand)
				if sInputedComand < 1 or sInputedComand > iAmmounOfTasksTask4():					
					print("Невірний пункт меню")
			except ValueError:
				print("Невірно вказане значення")
				sInputedComand = 0	
			###1
			if sInputedComand == 1:
				del List 
				List = []
				isCreatedList = True
				print("Done")				
			###2
			elif sInputedComand == 2:
				if isCreatedList == True:
					try:
						List.append(int(input("Element: ")))
					except ValueError:
						print("Невірне значення")				
				else:
					print("Необхідно створити список")
			###3
			elif sInputedComand == 3:
				if isCreatedList == True:
					print(List)
				else:
					print("Необхідно створити список")
			###4
			elif sInputedComand == 4:			
				print("Завершення роботи...")
				vLineSpacer("Кінець основного завдання")
				del List
				isCreatedList = False
				break
			###5
			elif sInputedComand == 5:
				try:					
					List = list(range(1, int(input("Введіть розмір масиву натуральних чисел: "))+1))
				except ValueError:
					print("Не правильне значення")
			###6
			elif sInputedComand == 6:
				if len(List) > 0:
					try:
						iDeletedIndex = int(input("Введіть індекст елементу для видалення: "))
						if iDeletedIndex >= 0 and iDeletedIndex < len(List):
							del List[iDeletedIndex]
						else:
							print("Некоректний індекс")
					except ValueError:
						print("Не правильне значення")
				else:
					print("Список не створено...")
### П'яте завдання
	elif iTask == 5:
		vLineSpacer("П'яте завдання")		
		lDictMenu = ["Dictionary menu", "\t1:Перевірити місто", "\t2:Список міст", "\t3:Кількість міст", "\t4:Видалити місто", "\t5:Список країн", "\t6:Додати елемент словника"]
		for i in lDictMenu:
			print(i)			
		sInputedDictComand = input('$:')

		iAmmounOfTasksTask5 = lambda : 6
		###
		try:
			sInputedDictComand  = int(sInputedDictComand )
			if sInputedDictComand  < 1 or sInputedDictComand  > iAmmounOfTasksTask5():
				print("Невірний пункт меню")
		except ValueError:
			print("Невірно вказане значення")
			sInputedComand = 0
		###.1
		if sInputedDictComand  == 1:
			sCityName = input("Введіть назву міста: ")
			if sCityName in Dictionary.keys():
				print("Таке місто є і воно знаходиться в %s"%(Dictionary[sCityName]))
			else: print("Такого міста немає...")
		###.2
		elif sInputedDictComand  == 2:
			print("Міста:", list(Dictionary.keys()))
		###.3
		elif sInputedDictComand  == 3:
			print("Кількість елементів словника: %d"%(len(Dictionary)))
		###.4
		elif sInputedDictComand  == 4:
			sCityName = input("Введіть назву міста: ")
			if sCityName in Dictionary.keys():
				del Dictionary[sCityName]
				print("Таке місто є і видалене")
			else: print("Такого міста немає...")
		###.5
		elif sInputedDictComand  == 5:
			print("Країни:", list(Dictionary.values()))		
		###.6
		elif sInputedDictComand  == 6:
			sCityName = input("Введіть назву міста: ")
			Dictionary[sCityName] = input("Введіть назву країни: ")
		vLineSpacer("Кінець п'ятого завдання")
###	
	iTask = 0