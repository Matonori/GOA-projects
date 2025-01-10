#2
list1 = [2, 4, 6, 8, 10]
double = list(map(lambda x: x * 2, list1))
print(double)

#3
list2 = ["Alice", "Bob", "Charlie"]
res = list(map(lambda x: "Hello, " + x, list2))
print(res)

#4
list3 = ["apple", "banana", "kiwi"]
length = list(map(lambda str1: len(str1), list3))
print(length)

#5
numbers = [-5, 3, -2, 7, 0, 10]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)

#6
list4 = ["pear", "apple", "peach", "grape"]
P = list(filter(lambda str2: str2[0] == "p", list4))
print(P)

#7
numbers = [10, 55, 42, 78, 65, 20]
greater = list(filter(lambda n: n > 50, numbers))
print(greater)

#8) ჩამოაყალიბეთ რა განსხვავებაა map'სა და filter'ს შორის
# map - ცვლის ლისტის ელემენტებს
# filter - მხოლოდ ფილტრავს ლისტის ელემენტებს