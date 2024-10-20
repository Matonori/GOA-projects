menu = ["salad", "pizza", "chicken", "steak", "fries"]
menu.remove("salad")
print(menu[0])
meat = slice(1, 3)
print(menu[meat])
print(menu)
#lists are used to store information.

passwords = ("JIPOL948", "POLIRON817", "HUADW221", "POLOL191", "LOSTFROMSUN1241")
# passwords.remove("JIPOL948")  <---- this doesnt work
print(passwords[0])
firsthalf = slice(1, 3)
print(passwords[firsthalf])
pass1 = passwords
print(pass1)

#tuples are used to store information that shouldn't be altered directly.

dice = {"one", "two,", "three", "four", "five", "six"}
dice.remove("one")
#print(dice[0]) <---- won't work because no Index
print(dice)
