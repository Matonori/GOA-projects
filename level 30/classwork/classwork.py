#name error- ეს ერორი ჩნდება როდესაც ვხმარობთ ცვლადის სახელს, რომელიც ჯერ არ არის შექმნილი
try:
    print(name)
except NameError:
    print("name is not defined")
#index error - ეს ერორი ჩნდება მაშინ, როდესაც ვცდილობთ ინდექსის გამოყენებას მაშინ, როდესაც ეს არ შეგვიძლია
try: 
    numbers = [10, 20, 30]
    numbers[4]
except IndexError:
    print("index can not be used with tuple")

#value error - გვხვდება როდესაც value type-ი არის სწორი, მაგრამ თავად value არა
try:
    num = int("forty-two")
except:
    print("the value needs to be a number with brackets around it")

#try გვადგება რომ შევამოწმოთ კოდი და აქვს თუ არა მას შეცდომა, ხოლო except გვეხმარება ეს კოდი შევასწოროთ