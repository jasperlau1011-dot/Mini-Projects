print("hello my name is big ed!")
name = input("whats your name?")
print("hello, " + name.title())
surname = input("whats your surname?")
full_name = name.title() + " " + surname.title()
print("Hello, " + full_name)
print("how old are you?")
age = int(input())
if age >= 12 and age < 100:
    print("your allowed")
if age < 12:
    print("bye bye!")
if age > 99:
    print("youre TOOOOOO old")
pet = input("what type of pets do you like?  dog,  cat,  fish")
if pet == "dog":
    print("i love doggggggggIieeeeeee!")
elif pet == "cat":
    print("cats are the best!")
elif pet == "fish":
    print("fish are nice!")
else:
    print("bruh")
import time 
time.sleep(2)
print("\nthis is my favourite food ingrediants:" + "\n\ttomatoe,\n\tegg,\n\tbread,\n\tand pork")
time.sleep(2)
print("\nheres the squares from 1-20:")
time.sleep(2)
for value in range(1, 21):
    print(value ** 2)
time.sleep(2)
print("\nthis is a lottery, pick number from 1-6")
lot = int(input())
import random
dice_roll = random.randint(1, 6)
if lot == dice_roll:
    print("you win!")
else:
    print("better luck next time!")
    trya = input("try again?")
    if trya == "yes" or "YES" or "Yes":
        lot_2 = int(input("pick number."))
        dice_roll = random.randint(1, 6)
        if lot_2 == dice_roll:
            print("you win!")
        else:
            print("no more chances!")
    else:
        print("ok")
print("\nend of chat. please press the play button above to complete the chat again.")
        
          

    





