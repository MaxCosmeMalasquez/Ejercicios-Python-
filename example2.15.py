print("Write your year")
x = int(input())
if x%4==0 and x%100 != 0 or x%400==0 : 
    print("It´s a leap year ")
else : 
    print("It´s not leap year ") 