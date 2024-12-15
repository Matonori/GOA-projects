try:
    print(name)
except NameError:
    print("name is not defined")

try: 
    numbers = [10, 20, 30]
    numbers[4]
except IndexError:
    print("index can not be used with tuple")

try:
    num = int("forty-two")
except:
    print("the value needs to be a number with brackets around it")

