from PIL import Image, ImageEnhance
from mathProcess import *

img = Image.open("C:/Users/Користувач/Pictures/Картинки/FVEnqVM.jpg")
imgMatrix = img.getdata()

lst = []
size = len(imgMatrix)
print("Ammount of pixels: " + str(size))
ii, k = 1, 1
i_rgb = lambda r, g, b, l0, l1, l2: (int(r*l0), int(g*l1), int(b*l2))
i_l = lambda r, g, b, l0, l1, l2: r*l0+g*l1+b*l2
for i in imgMatrix:
	if (ii/size)*100 > k*10:
		print("%.2f %% completed..."%((ii/size)*100))
		k+=1
	#lst.append(i_r(i[0], i[1], i[2]))
	#lst.append(i_l(i[0], i[1], i[2], 0.4, 0.5, 0.01))
	ii+=1

newImg = Image.new("RGB", img.size)
newImg.putdata(lst)
#newImg.show()

data = [2, 4, 4, 4, 4, 5, 6, 7, 8, 9]
print(mathProcess.mode(data))
