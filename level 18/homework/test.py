word = "hello world"
print(word.upper())
print(word[0].upper())

print(word.upper())
# Turns every letter to its uppercase variant.

print(word.lower())
# Turns every letter to its lowercase variant.

print(word.capitalize())
# Capitalizes the first letter, while making all other letters lowercase.

print(word.swapcase())
# Makes lowercase letters uppercase and uppercase letters lowercase.

print(word.find("h"))
# Finds the value stored in ()s in a variable.

list = [1, 2, 3]
print(len(list))
print(len(word))

# Figures out the length of a list/variable.

print(list.index(1))
# Figures out the index of a provided argument.

list.append(4)
print(list)
# Adds an entry at the end of the list.

list.insert(4, 9)
print(list)
# Inserts an entry at a provided index.

list.pop(1)
print(list)
# Removes an entry in a list using a provided index.

list.remove(1)
print(list)
# Removes an entry in a list using a provided value from the list.