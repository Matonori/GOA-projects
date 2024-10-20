tuple1 = (1, 2, 3)
num1, num2, num3 = tuple1
print(num1)

tuple2 = (19, 23, 42, 12)
one, *ha = tuple2
print(ha)
#the symbol "*" in this case is used as a "rest" operator.

dice = {1, 2, 3, 4 , 5, 6}
print(dice)



# list-ის თვისებები არის:
# ლისტის ელემენტებს ენიჭებათ ინდექსები
# შეგივიძლია გამოვიყენოთ ეს ინდექსები და slicing
# ლისტში შეიძლება იყოს დუპლიკატები
# ლისტი აღინიშნება []-ით
# ლისტი არის mutable (შეგვიძლია ცვლილებები შევიტანოთ ფუნქციებით, როგორიცაა apend)

# tuple-ის თვისებები არის:
# თუფლის ელემენტებს ენიჭებათ ინდექსები
# შეგივიძლია გამოვიყენოთ ეს ინდექსები და slicing
# თუფლში შეიძლება იყოს დუპლიკატები
# თუფლი აღინიშნება ()-ით
# თუფლი არის immutable (არ შეგვიძლია ცვლილებები შევიტანოთ ფუნქციებით, როგორიცაა apend)

# set-ის თვისებები არის:
# სეტის ელემენტებს არ ენიჭებათ ინდექსები
# არ შეგივიძლია გამოვიყენოთ ეს ინდექსები და slicing
# თუფლში არ შეიძლება იყოს დუპლიკატები
# თუფლი აღინიშნება {}-ით
# თუფლი არის mutable


# მსგავსებები ლისტსა და თუფლს შორის:
# ელემენტებს ენიჭებათ ინდექსები
# შეგივიძლია გამოვიყენოთ ეს ინდექსები და slicing
# თუფლში შეიძლება იყოს დუპლიკატები
# ორივე გამოიყენება მონაცემების შესანახად

# განსხვავებები:
# ლისტი არის mutable, თუფლი კი არა.
# ლისტი აღინიშნება []-ით, თუფლი კი ()

# მსგავსებები ლისტსა და სეტს შორის:
# ორივე გამოიყენება მონაცემების შესანახად
# ორივე არის mutable

# განსხვავებები:
# სეტში არ შეიძლება იყოს დუპლიკატები
# სეტი არის onordered, (დაულაგებელი), ამიტომ ლისტისგან განსხვავებით არ ენიჭება ინდექსები მის ელემენტებს.
# სეტი აღინიშნება {}-ით.

tuple3 = (1, 2, 3)
#tuple3.add(4) <------- error
#tuple3.remove(1) <------- error
print(tuple3)

set = {1, 2, 3}
set.add(4)
set.remove(3)
print(set)

