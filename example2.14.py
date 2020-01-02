import math
print("First side of the triangle")
x = int(input())
print("Second side of the triangle")
y = int(input())
print("Third side of the triangle")
z = int(input())
if  x**2 == math.sqrt(y**2+z**2): 
    print("It is the right triangle")
elif x==y or x==z or  y==z:
    print("It is an isosceles triangle")
elif x==y==z : 
    print("It is the equilateral triangle")
else : 
    print("It is the scalene triangle ")

