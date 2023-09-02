import math
a = 60
math.pow(a,2)
3600.0
import random
b = random.randint(5, 50)
b
11
a = 25
math.sqrt(a)
5.0
# Python program to calculate distance between two points
x1 = float(input("Enter the x1 value: "))
x2 = float(input("Enter the x2 value: "))
y1 = float(input("Enter the y1 value: "))
y2 = float(input("Enter the y2 value: "))
# Display the co-ordinates of two points
print("Co-ordinates of first point are (",x1, ",", y1,")")
print("Co-ordinates of second point are (",x2, ",", y2,")")
# Calculate distance between two points
r = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))
print("Distance between two points is ", r)