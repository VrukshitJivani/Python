 #write a program to figure out whether given number  is perfect number or not
#A perfect number is a positive integer that is equal to the sum of its proper divisors.
#The smallest perfect number is 6, which is the sum of 1, 2, and 3.(1+2+3=6)

tmp=0
num=int(input("Enter number :"))
tmp=num
sum=0
i=1
half=(num//2)+1
while i<half:
    if num%i==0:
        sum=sum+i 
    i+=1 

if tmp==sum:
    print("Number is perfect ")
else:
    print("Number is not perfect")