# print("Write the date")
# print("¿How long is the call? " )
# x =int(input())
# print("¿It´s Sunday ? (Y/N):")
# y = input()
# if y.upper() == "N":
#     z = input(" ¿What shift:Morning or afternoon? (M/A)")
# if x <= 5 : 
#     precio = x * 1 
# elif x <= 8 : 
#     precio = (x-5)*0.80
# elif x <= 10 : 
#     precio = (x-8) *0.70 
# else :
#     precio = (x-10) * 0.50 
# if y.upper() =="Y" :
#     precio = precio + precio *0.03 
# else : 
#     if  z.upper()== "M" :
#         precio = precio+ precio *0.15 
#     else : 
#         precio = precio *0.10 
# print("Price of talk is $"  + str(precio))

print("Write the date")
print("¿How long is the call? " )
x =int(input())
if x <= 5 : 
    precio = x * 1 
elif x <= 8 : 
    precio = (x-5)*0.80
elif x <= 10 : 
    precio = (x-8) *0.70 
else :
    precio = (x-10) * 0.50 
print("¿It´s Sunday ? (Y/N):")
y = input()
if y.upper() =="Y" :
    precio = precio + precio *0.03
elif y.upper() == "N":
    print(" ¿What shift:Morning or afternoon? (M/A)")
    z = input()
else : 
    if  z.upper()== "M" :
        precio = precio+ precio *0.15 
    else : 
        precio = precio *0.10 
 
print("Price of talk is $"  + str(precio))





