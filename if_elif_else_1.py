purchase_price=int(input("Enter purchase price :"))
selling_price=int(input("Enter selling price :"))
diffrence=selling_price-purchase_price
if diffrence>0:
    print("Profite amount is ",diffrence)
elif diffrence<0:
    print("Lose amount is ",diffrence)
else:
    print("No profite No Loss")