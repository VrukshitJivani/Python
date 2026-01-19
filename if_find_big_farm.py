length1=int(input("Enter 1st farm length:"))
weigth1=int(input("Enter 1st farm weigth:"))

length2=int(input("Enter 2nd farm length:"))
weigth2=int(input("Enter 2nd farm weigth:"))

area_first_farm=length1*weigth1
area_second_farm=length2*weigth2

if area_first_farm>area_second_farm:
    print("Fisrt farm is bigger than second farm")
else:
    print("Second farm is bigger than first farm")
