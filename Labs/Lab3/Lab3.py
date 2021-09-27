from tasks import TaskOne

printLine = lambda len: print("+" + "-"*(len-2)+ "+")
while True == True:
    task = 0
    try:
        task = int(input("Введіть номер завдання(1/2/3/-1): "))
    except Exception:
        pass
    
    #завдання 1
    if task == 1:
        def printListOfGoods():
            print("|Список товарів")
            printLine(49)
            for i in listOfGoods:
                print("|Товар: %s\t\t|Ціна: %d\t\t|"%(i[0], i[1]))
            printLine(49)
            print("check \t- виводить ваш чек", "ok \t- завершує процес уведення товарів", sep='\n')
        #
        listOfGoods = []
        listOfGoods.append(["Banana".upper(), 20])
        listOfGoods.append(["Kiwi".upper(), 50])
        listOfGoods.append(["Mango".upper(), 38])
        listOfGoods.append(["Coconut".upper(), 25])
        listOfGoods.append(["Apple".upper(), 22])
        listOfGoods.append(["Peach".upper(), 45])
        #
        listOfCustomer = []
        printListOfGoods()
        #
        while True == True:
            customerInput = input("Введіть назву товару та його вагу(щоб зменшити, уведіть - перед значенням): ")
            customerInput = customerInput.split()    
            if len(customerInput) > 1:
                #перевірка наявності товару
                isGoodsReaded = False
                for i in range(len(listOfCustomer)):
                    if customerInput[0].upper() == listOfCustomer[i][0]:
                        isGoodsReaded = True
                        try:
                            customerInput[1] = float(customerInput[1])
                            #товар, вага, ціна
                            listOfCustomer[i][1] += customerInput[1]
                            if listOfCustomer[i][1] == 0:
                                del listOfCustomer[i]
                            print("Кількість товару змінена")
                            break
                        except Exception:
                            print("Неможливо зчитати вагу товару...")
                if isGoodsReaded == False:
                    for i in listOfGoods:
                        if customerInput[0].upper() == i[0]:
                            isGoodsReaded = True
                            try:
                                customerInput[1] = float(customerInput[1])
                                #товар, вага, ціна
                                listOfCustomer.append([customerInput[0].upper(), customerInput[1], i[1]])
                                print("Товар успішно додано")
                                break
                            except Exception:
                                print("Неможливо зчитати вагу товару...")
                if isGoodsReaded == False:
                    print("Такого товару не існує...")
            elif customerInput[0] == "check":        
                if len(listOfCustomer) > 0:
                    print(listOfCustomer)
                    print("|Чек")
                    printLine(97)
                    for i in listOfCustomer:
                        print("|Товар: %s\t\t|Вага: %.3f\t\t|Ціна: %d\t\t|Сума: %.3f\t\t|"%(i[0], i[1], i[2], i[1]*i[2]))
                    printLine(97)
            elif customerInput[0] == "ok":
                break        
    elif task == 2:
        #
        dictStud = {}
        dictStud["John Doe#1"] = [4, 5, 3]
        dictStud["John Doe#2"] = [2, 4, 5, 5]
        dictStud["John Doe#3"] = [4, 3, 1]
        dictStud["John Doe#4"] = [5, 2, 5, 2]
        dictStud["John Doe#5"] = [3, 2, 5, 2]
        dictStud["John Doe#6"] = [3, 5, 5, 4]
        #
        duty = 0
        dictStud_new = {}
        for stud in dictStud:
            mid = sum(dictStud[stud])/len(dictStud[stud])            
            dictStud_new[stud] = mid
            if mid < 3.0:
                duty+=1
        print("Кількість заборгованостей %d"%(duty))
        for stud in dictStud_new:
            print("Середній бал %s: %.1f"%(stud, dictStud_new[stud]))
    elif task == 3:        
        #
        listDictGroup = []
        listDictGroup.append({"surname":"Doe#1", "name":"Jane", "marks":[5, 1, 4]})
        listDictGroup.append({"surname":"Doe#2", "name":"Jake", "marks":[3, 4, 2]})
        listDictGroup.append({"surname":"Doe#3", "name":"John", "marks":[5, 3, 2]})
        listDictGroup.append({"surname":"Doe#4", "name":"Jiah", "marks":[4, 2, 5]})
        listDictGroup.append({"surname":"Doe#5", "name":"Jeera", "marks":[2, 5, 4]})
        #2
        print(listDictGroup[0])
        #3
        for i in listDictGroup:
            print(i["surname"].ljust(10), i["name"].ljust(8), i["marks"])
        #4|5
        listMidMarks = []
        for i in listDictGroup:
            listMidMarks.append([i["surname"], sum(i["marks"])/len(i["marks"])])
        #6
        listSurnames = []
        for i in listDictGroup:
            listSurnames.append(i["surname"])
        #7
        allMidMark = 0
        for i in listMidMarks:
            allMidMark += i[1]        
        allMidMark /= len(listMidMarks)
        print("Середня оцінка %.1f"%(allMidMark))
    elif task == -1:
        break