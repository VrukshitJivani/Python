def getInch(meter,foot=10,Inches=30):
    print(f"Meter:{meter} foot:{foot} Inches:{Inches} ")
    totalinches= meter*39.37 + foot*12 + Inches
    return totalinches
    
print(getInch(10,20,30))
print(getInch(20,30))
print(getInch(10))