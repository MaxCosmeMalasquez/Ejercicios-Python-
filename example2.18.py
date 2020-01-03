print("!Study trip!")
print("Number of students")
x =int(input())
if x>=100 : 
    print("The price of the trip will be : $ " + str(65*x) + " and price for each students is $65")
elif x>=50 and x <= 99 :
    print("The price of the trip will be : $" + str(70*x) + " and price for each students is $70")
elif x>=30 and x<=49 : 
    print("The price of the trip will be : $ " + str(95*x) + " and price for each students is $95")
else : 
    print("The price of the trip will be : $4000  and price for each students is " + str(4000/x)) 
