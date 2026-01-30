"""write a program to create 
function that calculate and return
simple interest of given amount
rate and year
"""

def getSI(P,R,N):
    si=P*R*N/100
    return si
    
p=int(input("Enter P :"))    
r=int(input("Enter R :"))
n=int(input("Enter N :"))

simple=getSI(p,r,n)
print("Simple Interest is ",simple)