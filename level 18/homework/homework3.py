list = [1, 2, 3, 4]
sum = 0
for i in list:
    sum += i
print(sum)


word = "Hello, world!"
for i in word:
    print(i)


for i in range(1, 101):
    if i < 50 or i > 60:
        print(i)

n=1
while n<51:
    print(n)
    n=n+1




n = int(input("choose a number: "))
if n / 3 == int(n / 3):
    print("this number is divisible by 3")
else:
    print("this number is not divisible by 3")
if n / 5 == int(n / 5):
    print("this number is divisible by 5")
else:
    print("this number is not divisible by 5")



def average(num1, num2, num3):
    list2 = [num1, num2, num3]
    num4 = len(list2)
    sum = 0
    for i in list2:
        sum += i
    print(sum / num4)

average(3, 4, 5)