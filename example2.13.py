import math
print("Write the first coordinate of the first circle")
x_1 = int(input())
print("Write the second coordinate of the first circle ")
y_1 =int(input())
print("Write the first coordinate of the second circle")
x_2 = int(input())
print("Write the second coordinate of the second circle")
y_2 = int(input())
print("Write the first radius of the first circle")
r_1 = int(input())
print("Write the first radius of the first circle")
r_2 = int(input())
distance = math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
suma_radios = (r_1+r_2)
print( " The distance is " + str(distance))
if distance > suma_radios : 
    print("It is external type ")
elif distance == suma_radios : 
    print("it is of external tangent type")
elif distance<suma_radios and distance>abs(r_1-r_2):
    print("It is secant type")
elif distance == abs(r_1-r_2):
    print("It is indoor Tangents")
elif distance>0 and distance<abs(r_1-r_2):
    print("It is indoor")
else : 
    print("It is concentric")
