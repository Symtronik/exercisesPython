# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi

radius = float(input("Enter the radius:"))
areaOfTheCircle = pi * radius**2


print(f"Area of the circle is {areaOfTheCircle}")