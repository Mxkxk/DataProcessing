import pandas as pd

data = pd.read_excel(pd.ExcelFile("KN-4.xlsx"))
print("Розмір таблиці %dx%d"%(len(data.columns), data.size/len(data.columns)))
print("Назви колонок : " + "|".join(data.columns))
data.fillna(0, inplace = True)
data.loc[:, "Test"] = [test/100*12 for test in data.loc[:, "Test"]]
data.loc[data["Lab1"] == "+", "Lab1"] = 2
data.loc[data["Lab2"] == "+", "Lab2"] = 2
print(data)
data[["L71", "L72"]] = data["Lab7"].str.split("/", expand = True)
data["L71"] = pd.to_numeric(data["L71"])
data["L72"] = pd.to_numeric(data["L72"])
sample = ["Lab1", "Lab2", "L71", "L72", "Test"]
data["Sum"] = [sum([float(data.loc[n, d]) for d in sample]) for n in range(int(data.size/len(data.columns)))]
data = data.rename(columns = {"Lab7":"L7"})
print("Найбільша сума %.2f"%(data["Sum"].max()))
print("Індекс найбільшої суми %d"%(data[data["Sum"] == data["Sum"].max()].index[0]))
print("Студент з найбільшою сумою: %s"%(list(data.loc[data["Sum"] == data["Sum"].max(), "Student"])[0]))
print(data.loc[data["Sum"] == 0])
print(data.loc[data["Sum"] > 15])
print("Кількість студентів з сумою балів більше 15: %d"%(len(data.loc[data["Sum"] > 15])))
print(data[data["Lab1"].isin([2])])
data["Lab4"] = 2
print(data)
print(data.loc[:, ["Student", "Sum"]])
data["Dopusk"] = data["Sum"] > 15
print(data)