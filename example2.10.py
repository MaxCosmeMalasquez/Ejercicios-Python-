print("Write the base")
x = int(input())
print("Write the exponent")
y = int(input())
if y > 0 : 
    print(" The result is " + str(x**y))
elif y < 0 : 
    print("The result is " + str(1/x**-y))
else :    
    print("The result is  " + str(1))