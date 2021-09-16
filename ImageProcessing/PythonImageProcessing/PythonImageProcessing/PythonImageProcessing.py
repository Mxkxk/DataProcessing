from PIL import Image, ImageEnhance

img = Image.open("C:/Users/Користувач/Pictures/Картинки/FVEnqVM.jpg")
imgMatrix = img.getdata()

lst = []
size = len(imgMatrix)
print("Ammount of pixels: " + str(size))
ii, k = 1, 1
i_rgb = lambda r, g, b: (int(r*0.2), int(g*0.8), int(b*0.1))
i_l = lambda r, g, b, l0, l1, l2: r*l0+g*l1+b*l2
for i in imgMatrix:
	if (ii/size)*100 > k*10:
		print("%.2f %% completed..."%((ii/size)*100))
		k+=1	
	#lst.append(i_r(i[0], i[1], i[2]))
	lst.append(i_l(i[0], i[1], i[2], 0.2, 0.7, 0.1))
	ii+=1

newImg = Image.new("L", img.size)
newImg.putdata(lst)
newImg.show()
