import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


plt.figure(figsize=(10,6))
#1
#data_pi = np.linspace(-np.pi, np.pi, 100)
#sin_ = np.sin(data_pi)
#cos_ = np.cos(data_pi)

#plt.plot(data_pi, sin_, color="red", ls=":", linewidth=3)
#plt.plot(data_pi, cos_, color="green", ls="--", linewidth=3)
#plt.title("sin, cos")
#plt.xlabel("проміжок від -п до п", color="#00F", size=18)
#plt.ylabel("значення функції", color="#00F", size=18)
#2
#data_pie_names = ['Zelensky', 'Poroshenko', 'Tymoshenko', 'Boyko', 'Hrytsenko', 'Smeshko', 'Lyashko', 'Vilkul', 'other']
#data_pie_votes = [30.24, 15.95, 13.4, 11.67, 6.91, 6.04, 5.48, 4.15]
#last = 100
#for i in data_pie_votes:
#	last = last - i
#data_pie_votes.append(last)
#plt.pie(data_pie_votes, labels=data_pie_names, autopct='%.1f%%', explode=[0.05]+[0 for i in range(len(data_pie_names)-1)])
#plt.title("Result of first tour of 2019 elections")
#3
#data_csv = pd.read_csv('coronovarus.csv')
#print(data_csv)
#plt.bar(data_csv['Date'], data_csv['New cases'])
#plt.grid()
#plt.title('Коронавірус в Україні')
#plt.gca().set_xticklabels(labels=data_csv['Date'], rotation=30)
#plt.subplots_adjust(bottom=0.15)
#4
#bar = plt.bar(data_csv['Date'], data_csv['New cases'])
#plt.grid()
#plt.title('Coronavirus/Ukraine', color="#00F")
#plt.xlabel(data_csv.columns[0], color="#00F")
#plt.ylabel(data_csv.columns[1], color="#00F")
#plt.gca().bar_label(bar, padding=-15, color="#000")
#5
#fig = plt.figure()
#sb_1 = fig.add_subplot(3, 1, 1)
#sb_1.plot()
#sb_1.set_xlim(0, 1)
#sb_1.set_ylim(0, 1)
#sb_2 = fig.add_subplot(3, 3, 4)
#sb_2.plot()
#sb_2.set_xlim(0, 1)
#sb_2.set_ylim(0, 1)
#sb_3 = fig.add_subplot(3, 3, 6)
#sb_3.plot()
#sb_3.set_xlim(0, 1)
#sb_3.set_ylim(0, 1)
#sb_4 = fig.add_subplot(3, 1, 3)
#sb_4.plot()
#sb_4.set_xlim(0, 1)
#sb_4.set_ylim(0, 1)
#6
fig = plt.figure()
sb = fig.add_subplot(111, projection="3d")
x = np.linspace(-1, 1, 50)
y = np.linspace(-2, 2, 50)
def zfun(x, y):	
	return x**3+x*(y**2)
X, Y = np.meshgrid(x, y)
zs = np.array(zfun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)
sb.plot_surface(X, Y, Z, cmap='viridis')
plt.title("Z = X**3 + X*(Y**2)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("somefig", dpi=300)
plt.show()
