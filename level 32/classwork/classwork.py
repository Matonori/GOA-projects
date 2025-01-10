#Level 32:
#1) შექმენით ანონიმური ფუნქცია რომელიც გამოიტანს 2 რიცხვის ჯამს
def sum(x, y):
    return print(x + y)
sum(2, 4)

#2) შექმენით ანონიმური ფუნქცია რომელიც გააორმაგებს გადაცემულ რიცხვს 
def timestwo(x):
    return print(x*2)
timestwo(7)

#3) შექმენით ანონიმური ფუნქცია რომელიც მიიღებს start და end 
#პარამეტრებს და გამოიტანს list'ს რომელშიც იქნება რიცხვები 
# start'იდან end'მდე
def lab(start, end):
    lab = [x for x in range(start, end+1)]
    return print(lab)
lab(9, 11)

#4) გადახედეთ ამ მასალას და ეცადეთ გააკეთოთ ეს დავალება: 
#შექმენით map ფუნქცია რომელიც list'ში ყველა რიცხვს გაასამმაგებს.
normal = [1, 2, 3, 4, 5]
triple = list(map(lambda x: x * 3, normal))
print(triple)