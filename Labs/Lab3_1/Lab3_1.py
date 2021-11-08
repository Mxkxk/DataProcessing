import numpy as np
import pandas as pd

table = pd.read_csv("olympics.csv", index_col=0, skiprows=1)
print(table)
table.info()
table = table.append(pd.DataFrame([], columns=table.columns, index=['Bangladesh\xa0(BGD)']))
table.fillna(0, inplace=True) 
table = table.rename(columns={"01 !":"Gold", "02 !":"Silver", "03 !":"Bronze"})
table = table.drop("Totals", axis=0)
newTable = pd.DataFrame(table.loc[:, ["Gold", "Silver", "Bronze"]], columns=["Gold", "Silver", "Bronze"], index=table.index)
print(newTable[newTable["Gold"] > 0])
print("Кількість країн з золотими медалями: ", len(newTable.loc[newTable["Gold"] > 0]))
print(newTable.loc[newTable["Gold"] == newTable["Gold"].max()].index[0])
print(newTable.loc[(newTable["Gold"]>0)&(newTable["Silver"]>0)])
print("Чи є в списку Україна? ", "Ukraine\xa0(UKR)" in newTable.index)