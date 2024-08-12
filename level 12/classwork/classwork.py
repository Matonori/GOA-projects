age = int(input("enter your age:"))
if age >= 18:
    print("normal price")
if age < 18:
    print("discount")

ticket = int(input("enter your ticket number:"))
if ticket == 6:
    print("You won a house")
if ticket == 30:
    print("you won a trip to hawai")
else:
    print("you won 1 dollars")

age = int(input("enter your age"))
student = input("are you a student?")
if age < 18 and student == "yes":
    print("discount")
else:
    print("standard price")
