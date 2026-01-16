#write a program to find profite or loss of given purchase price and selling price 
purchase_price=int(input("Enter purchase price:"))
selling_price=int(input("Enter selling price:"))

sell=selling_price-purchase_price
if sell>0:
    print("Profite")
if sell<0:
    print("Lose")
if sell==0:
    print("No profite and No loss")

