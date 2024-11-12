# ობიექტი არის რაიმე ფიზიკური ნივთი რომელსაც გააჩნია თავისი თვისებები
# dictionary გამოიყენება ამ ობიექტების აღსაწერად

mouse = {
    "item": "mouse",
    "color": "black",
    "light": "red",
    "battery": [2, "A"],
    "size(cm)": 15
}
print(mouse)
print(mouse.keys())
print(mouse.values())
print(mouse.items())


computer = {
    "item": "laptop",
    "color": "black",
    "mousepad": {
        "color": "black",
        "length(cm)": 10,
        "width(cm)": 20
    },
    "battery": [2, "A"],
    "size(cm)": 15
}
print(computer)
print(computer.keys())
print(computer.values())
print(computer.items())
print(computer["mousepad"])


keyboard = {
    "item": "keyboard",
    "color": "black",
    "keys": "black",
    "lights": "none",
    "price": "15 GEL"
}
print(keyboard)
print(keyboard.keys())
print(keyboard.values())
print(keyboard.items())

for i in mouse.keys():
    print(mouse[i])
for i in computer.keys():
    print(computer[i])
for i in keyboard.keys():
    print(keyboard[i])

for i in mouse.values():
    print(i)
for i in keyboard.values():
    print(i)
for i in computer.values():
    print(i)

for i in mouse.items():
    print(i)
for i in keyboard.items():
    print(i)
for i in computer.items():
    print(i)

for key, value in keyboard.items:
    print(key)
    print(value)

