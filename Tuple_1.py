#Tuple in Python is a collection which is ordered and unchangeable.It is only used to store multiple items and read only in a single variable.
# Creating a tuple of favorite fruits
favFruit=("apple","banana","orange","grape","mango","peach","kiwi","pear","plum","cherry","apple","banana","orange","grape","mango")
print(favFruit)

print(type(favFruit))

print(favFruit[0])
print(favFruit[3:])

print(favFruit.index('banana'))
print(favFruit.index('kiwi'))

print(favFruit.count('apple'))
print(favFruit.count('orange'))
