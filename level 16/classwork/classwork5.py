def user_age():
    return int(input("enter your age: "))

age = user_age()

if age <= 17:
    print("you are underage")
else:
    print("you are an adult")

