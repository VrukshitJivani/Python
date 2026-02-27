#exception handing 
count=0
loop =True
while loop:
    try:
        run=int(input("Enter run :"))
        ball=int(input("Enter ball :"))
        run_rate=run/ball*100
        print(run_rate)
        loop=False
    except ZeroDivisionError:
        print("you can not divide by zero to ball")
    except ValueError:
        print("Invalide value input ")
    finally:
        count+=1
        if count==5:
            print("You can attempt 5 invalide input")
            loop=False
