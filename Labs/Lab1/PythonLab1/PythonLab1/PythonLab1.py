import math

print("Input percent:")
h = int(input())
print("Angle of hill is " + str(round(math.degrees(math.asin(math.hypot(100/h, 1)**-1)))) + " degree")