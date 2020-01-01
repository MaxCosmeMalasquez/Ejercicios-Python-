print("Tell me your mark on the exam")
note = int(input())
if note >= 1 and note <=4 : 
    print("discontinued")
elif note == 5:
    print("enough")
elif note == 6 or note == 7 : 
    print("aprovved")
elif note == 8:
    print("Wonderful")
elif note == 9 or note == 10 : 
    print("Excellent")
else : 
    print("you are bad, you can´t write a note")