kit=["Water Bottle","Notebook","Pen","Hat",500];
Marks=[70,89,56,78,67,99,56,89]

print("Kit items:",kit)

#kit
print(kit[0])# Water Bottle

print(kit[1])# Notebook

kit.insert(4,"Snacks")# Insert Snacks at index 4
print(kit)

kit.remove("Water Bottle")# Remove Water Bottle
print(kit)

kit.pop(3)# Remove item at index 3
print(kit)

print(kit.index("Hat"))# Get index of Hat

kit.append("Laptop")# Add Laptop at the end
print(kit)

#Marks
print("Marks:",Marks)
print(Marks[2])# 56
print(Marks[5])# 99
print(Marks[0:4])

Marks.sort()# Sort the list
print(Marks)

# Count occurrences of 56
print(Marks.count(56))

Marks.reverse()# Reverse the list
print(Marks)

del Marks[2]# Delete item at index 2
print(Marks)

