import random

range_=input("Type a number: ")

if range_.isdigit():
    range_=int(range_)

    if range_<=0:
        print("Please enter num greater than 0 next time")
        quit()
else:
    print("Enter a number,not a string")
    quit()

random_val=random.randint(1,range_)
print("Numbers will be generated between 1 to",range_)
print("You are supposed to guess the number in min turns ")
print("As soon as the generated number gets matched with the number you entered","\n A prompt will display your min guesses")
no_turns=0
while True:
    no_turns+=1
    entered_val=input("Enter the number")
    if int(entered_val)<random_val:
        print("guess higher")      
    elif int(entered_val)>random_val:
        print("guess lower")
    else:
        break


print("you got the number correct in ",no_turns,"guesses")



