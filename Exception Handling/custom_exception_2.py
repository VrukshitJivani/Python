class bankExceptiom(Exception):
    pass

balance=400000
daily_limit=100000

amount=int(input("Enter Amount,you want to transfer!"))
try:
    if amount>balance:
        raise bankExceptiom("Insuficient Balance!")
    elif  amount>daily_limit:
        raise bankExceptiom("You crosed your daily limit!")
    else:
        print("Your remaining balance :",balance-amount)
        print("Thank you for banking us!")
except bankExceptiom as error:
    print(error)
    
    
    