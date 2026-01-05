favDesti=['Rajsthan','Goa','Junagadh','Kashmir','Manali'];
favFruit=['Mango','Banana','Apple','Grapes','Orange'];

print(favDesti)
print(favDesti[0])
print(favDesti[1])
print(favDesti[0:3])
print(favDesti[3:])
print(favDesti[:4])
print(favFruit[0])
print(favFruit[1])
print(favFruit[1:4])
print(favDesti+favFruit)
print(favDesti*2)

favDesti3=favDesti# Assign favDesti to favDesti3
print(favDesti3)

favDesti.clear()
print(favDesti3)# favDesti3 will also be cleared

favFruit1=favFruit.copy()# Copy favDesti to favDesti1
print(favFruit1)

favFruit.clear()# Clear all items from favDesti
print(favFruit)

print(favFruit1)# favDesti1 will remain unchanged
