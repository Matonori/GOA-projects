def user_score():
    return int(input("enter your score: "))

age = user_score()

if age <= 79:
    print("you failed")
else:
    print("you passed")

