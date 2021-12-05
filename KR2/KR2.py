import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('2020.csv')
print(data.info())#виведення назв колонок

for i in data.columns:
	if 'Explained' in i or 'Dystopia' in i or 'whisker' in i or 'error' in i:
		del data[i]#видалення непотрібних колонок
print(data.info())#виведення назв колонок після відкидання зайвої інформації
#дослідження
setOfRegion = set(data['Regional indicator'])#отримання назв регіонів
mostHappyByRegion = [data[data['Regional indicator']==i].values[0][0:3] for i in setOfRegion]#отримання найщасливіших країн з конкретних регіонів та індекс щастя
mostHappyByRegion = pd.DataFrame(mostHappyByRegion, columns = data.columns[0:3]).sort_values([data.columns[2]], ascending=False).reset_index()#їх сортування від більшого до меншого
del mostHappyByRegion['index']
print(mostHappyByRegion)

mostLongLivedCountry = data.sort_values(['Healthy life expectancy'], ascending=False)#посортовано в порядку спадання за очікуваною тривалістю життя
listOfCols = [i for i in data.columns[2:len(data.columns)] if i != 'Healthy life expectancy']
liveExpCorr = [mostLongLivedCountry['Healthy life expectancy'].corr(mostLongLivedCountry[i]) for i in listOfCols]#обчислення кореляції показників та очікуваної тривалості життя
liveExpCorrDF = pd.DataFrame(liveExpCorr, listOfCols, ['Correlation']).sort_values('Correlation', ascending=False)#датафрейм посортований за впливом на очікувану тривалість життя
print(liveExpCorrDF)

Values = [data.groupby('Regional indicator').sum()[i] for i in data.columns[2:len(data.columns)]]#список суммарних значень по группах регіонів
ValuesDF = pd.DataFrame(data=Values).transpose()#створення датафрейму
print(ValuesDF['Freedom to make life choices'])

midValues = [data.groupby('Regional indicator').sum()[i]/data.groupby('Regional indicator').count()[i] for i in data.columns[2:len(data.columns)]]#список середніх значень по группах регіонів
midValuesDF = pd.DataFrame(data=midValues).transpose()#створення датафрейму
print(midValuesDF['Freedom to make life choices'])

plt.figure(figsize=(12,6))

#1
#labels_bh = [mostHappyByRegion.values[i][0] if len(mostHappyByRegion.values[i][0].split()) < 3 else " ".join(mostHappyByRegion.values[i][0].split()[0:2]) for i in range(len(mostHappyByRegion['Country name']))]
#barHappy = plt.bar(labels_bh, mostHappyByRegion['Ladder score'], color="purple")
#plt.grid()
#plt.title("Найвищі індекси щастя країн з кожного регіону", size=18)
#plt.gca().set_xticklabels(labels=labels_bh, rotation=30, size=14)
#plt.subplots_adjust(bottom = 0.2)
#plt.savefig("happyBars", dpi=300)

#2
#plt.scatter(listOfCols, liveExpCorrDF['Correlation'], color="orange", s=300)
#plt.title('Кореляція очікуваної тривалості життя та індекса щастя/решти чинників', size=18)
#plt.grid()
#plt.savefig("correlation", dpi=300)


#3
#plt.subplot(2, 1, 1)
#plt.title("Доля вкладу суммарного та середнього значення свободи вибору країн регіону", size=14)
#plt.pie(ValuesDF['Freedom to make life choices'], labels=ValuesDF.reset_index()['Regional indicator'])
#plt.subplot(2, 1, 2)
#plt.pie(midValuesDF['Freedom to make life choices'], labels=midValuesDF.reset_index()['Regional indicator'])
#plt.savefig("libertyVals", dpi=300)

plt.show()