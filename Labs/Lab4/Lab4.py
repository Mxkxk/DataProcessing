def outputMatrix(matrix, joinArg, height):
	for i in range(height):
		print(joinArg.join(map(str, matrix[i])))
printLine = lambda n: print("--"+str(n)+"-"*40)
#1
height = 5
matrOne = [[0 for j in range(4)] for i in range(height)]
printLine(1)
outputMatrix(matrOne, " ", height)
#2
matrTwo = [[i for j in range(6)] for i in range(height)]
printLine(2)
outputMatrix(matrTwo, " ", height)
#3
matrTree = [[j for j in range(6)] for i in range(height)]
printLine(3)
outputMatrix(matrTree, " ", height)
#4
height = 4
matrFour = [[j+i for j in range(5)] for i in range(height)]
printLine(4)
for i in matrFour:
	print(i)
#5
matrFifth = [[j%2 if i%2 else (1-j%2) for j in range(5)] for i in range(height)]
printLine(5)
for i in matrFifth:
	print(i)
#6
matrSixth = [[j+i*5 for j in range(5)] for i in range(height)]
printLine(6)
for i in matrSixth:
	print(i)
#7
height = 5
matrSeventh = [[j if i<j else i for j in range(5)] for i in range(height)]
printLine(7)
outputMatrix(matrSeventh, " ", height)
#8
height = 4
matrEighth = [[(j+i*2)%3 for j in range(5)] for i in range(height)]
printLine(8)
outputMatrix(matrEighth, " ", height)
#9
matrNinth = [[1 if j<=i else 0 for j in range(5)] for i in range(height)]
printLine(9)
outputMatrix(matrNinth, " ", height)
#10
height = 5
matrTenth = [[abs(j-i) for j in range(5)] for i in range(height)]
printLine(10)
outputMatrix(matrTenth, " ", height)
#10
matrTenth = [[1 if j in range(i-1, i+2) else 0 for j in range(5)] for i in range(height)]
printLine(10)
outputMatrix(matrTenth, " ", height)
#11
height = 4
matrEleventh = [[1 if j>i else 0 for j in range(4)] for i in range(height)]
printLine(11)
for i in matrEleventh:
	print(i)
#12
matrTwelweth = [[j*4+i for j in range(4)] for i in range(height)]
printLine(12)
for i in matrTwelweth:
	print(i)
#13
matrThirdteenth = [[j*4+3-i for j in range(4)] for i in range(height)]
printLine(13)
for i in matrThirdteenth:
	print(i)
#14
height = 5
matrFourteenth = [[1 if j%2 == 0 and i%2 == 0 else 0 for j in range(5)] for i in range(height)]
printLine(14)
for i in matrFourteenth:
	print(i)
#15
height = 5
matrFourteenth = [[1 if j%2 == 0 and i%2 == 0 else 0 for j in range(5)] for i in range(height)]
printLine(14)
for i in matrFourteenth:
	print(i)