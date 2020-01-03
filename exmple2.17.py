print("Product")
x = input()
print("Product : " + str(x))
print("Amount of money")
w = int(input())
print("type of product")
y =input()
#if y== "A" and y== "B":
   # print("Type of product is : " + str(y))
#else : 
   # print(" It isn´t part of the product type area ")
print("Product size")
z =int(input())
if y=="A" and z==1: 
    print("Profit earned: " + str (w+0.20))
elif y=="A" and z==2:
    print("Profit earned: " + str(w+0.30)) 
elif y=="B " and z==1: 
    print("Profit earned: " + str (w-0.30))
elif y=="B" and z==2:
    print("Profit earned: " + str(w-0.50))
else : 
    print("ERROR")


