# print("Exports and Imports Cosme")
# print("Destination zone ")
# x =int(input())
# print("Package Weight in grams")
# y = int(input())
# if x == 1  :
#     print(" Zone North America $ " + str(24*y))
# elif x == 2 : 
#     print("Zone Central America $ " + str(20*y))
# elif x==3 : 
#     print("Zone Latam $ " + str(21*y))
# elif x==4 : 
#     print("Zone Europe $ " + str(10*y))
# elif x== 5 : 
#     print("Zone Asia $ " +str(18*y))
# elif y > 5000 : 
#     print("Exceed Limit")
# else :
#     print(" Other Destinations")
# print("Package Weight in grams")
print("Exports and Imports Cosme")
print("Destination zone ")
x =int(input())
if x == 1  :
    print(" Zone North America")
elif x == 2 : 
    print("Zone Central America ")
elif x==3 : 
    print("Zone Latam ")
elif x==4 : 
    print("Zone Europe ")
elif x== 5 : 
    print("Zone Asia ")
else :
    print(" Other Destinations")
print("Package Weight in grams")
y = int(input())
if x == 1  and y <=5000: 
    print("Proceed your shipment and price is $ " + str(24*y))
elif x==2 and y<= 5000 : 
    print("Proceed your shipment and price is $ " + str(20*y))
elif x==3 and y<=5000 :
    print("Proceed your shipment and price is $ " + str(21*y))
elif x==4 and y<=5000 :
    print("Proceed your shipment and price is $ " + str(10*y))
elif x==5 and y<=5000 : 
    print("Proceed your shipment and price is $ " +str(18*y))
else :
    print("Exceed Limit")  



