'''
write a program to figure out whether given number is prime number or not 
'''
number=int(input("Enter number :"))
i=2
flage=0
half=(number//2)+1
while(i<half):
    if(number%i==0):
        flage=flage+1
    i=i+1
if(flage==0):
    print("Number is prime ")
else:
    print("Number is not prime ")
    
