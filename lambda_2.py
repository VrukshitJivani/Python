getSI=lambda p,r,n:p*r*n/100

p=int(input("Enter priciple:"))
r=int(input("Enter rate:"))
n=int(input("Enter period:"))
SI=getSI(p,r,n)
print("Simple interest is ",SI)