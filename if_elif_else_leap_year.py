#leap year 
#it divided by  4 
#it divided 100 and 400

year=int(input("Enter year :"))
if year>=1:
    if year%4==0 and year%100!=0:
        print("Is leap year")
    else:
        if year%100==0 and year%400==0:
            print("Is leap year")
        else:
            print("Is not leap year")
else:
    print("Invalide year")