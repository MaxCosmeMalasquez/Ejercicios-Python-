# print("Write first number")
# x = int(input())
# print("Write second number")
# y = int(input())
# print("Write third number")
# z= int(input())
# cadena = [x,y,z]
# cadena.sort() 
# print(cadena)

print("Write first number")
x = int(input())
print("Write second number")
y = int(input())
print("Write third number")
z= int(input())
if x>y and x>z and y>z : 
    print("The order is " + "[" + str(x)+"," +str(y)+ "," + str(z) + "]")
elif x>y and x>z and z>y :
    print(" The order is  " + "[" + str(x)+ "," + str(z) + "," + str(y) + "]")
elif y>x and y>z and x>z : 
    print(" The order is " + "[" + str(y)+ "," + str(x)+ "," + str(z) + "]")
elif y>x and y>z and z>x : 
    print(" The order is  " + "[" + str(y) + "," + str(z)+ "," + str(x) + "]")
elif z>x and z>y and x>y:
    print("The order is " + "[" +str(z) + "," + str(x) + "," + str(y) + "]")
else :  
    print(" The order is  " + "[" + str(z)+ "," + str(y) + "," + str(x) + "]")