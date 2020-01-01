print("Your first number")
x = int(input())
print(" Your Second number")
y = int(input())
if x >=0  and y>0:
    print("The result is " + str(x/y))
elif x == 0 :
    print("The result is " + str(x/y))
elif x< 0 and y < 0 : 
    print("The result is " + str (x/y))
elif x<0 and y>0 : 
    print("The result is " + str(x/y))
elif x> 0 and y<0 : 
    print("The result is " + str (x/y))
else : 
    print("Error , there is no division between  0 ")
