import random
attempts = 10  
number_secret =random.randint(1,100)
print("Write your number") 
entered_numbers =int(input()) 
while number_secret != entered_numbers and  attempts>1:
    if number_secret>entered_numbers:
        print("Very small")
    else : 
        print("Very high")
    attempts =attempts -1 
    print("He has left " , attempts,"attempts"  )    
    print("Guess the number(of one and one hundred):")
    entered_numbers= int(input())      
    if number_secret== entered_numbers:
        print("Perfect , you guessed in ")
    else :
        print("The number was " + str(number_secret))     
    
    
  
