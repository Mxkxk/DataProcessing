import packagePseudoMath

def countMarks(argsDict):
	mark = 0
	mark += sum([2  if d == "+" else 0 for d in argsDict])
	mark += int(argsDict["Lab3"].split("/")[0])+int(argsDict["Lab3"].split("/")[1])
	mark += int(argsDict["Test"])/5
	mark += int(argsDict["KR1"])
	return mark

csvFile = open("KN-2.csv", "r")
sCsvFile = csvFile.read().split("\n")
csvFile.close()
sCsvFile = [s.split(",") for s in sCsvFile]
sCsvFile = {sCsvFile[i][0]:countMarks({sCsvFile[0][j]:sCsvFile[i][j] for j in range(1, len(sCsvFile[i]))}) for i in range(1, len(sCsvFile))}
print(sCsvFile)
