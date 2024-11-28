list = [x ** 2 for x in range(1, 101)]
print(list)
for x in list:
    list2 = []
    if x % 2 == 0:
        list2.append(x)
print(list2)


