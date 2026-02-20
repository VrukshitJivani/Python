import generator as g

loop=True

while loop:
    print("1.Otp Generate \n2.Password Generate\n0.Exit\n")
    choise=int(input("Enter your choise :"))
    if choise==1:
        size=int(input("Enter size of opt where you want to generate  "))
        otp=g.otp_gen(size)
        print(otp)
    elif choise==2:
        size=int(input("Enter size of password where you want to  generate "))
        password=g.password_gen(size)
        print(password)
    elif choise==0:
        loop=False
    else:
        print("Invalid choise")
        
        
    