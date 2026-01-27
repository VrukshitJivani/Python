#write a program to figure out whether given number  is armstrong number or not
import math
num=int(input("Enter number :"))
tmp=num
r=0
sum=0
digit=len(str(num))
print("length is ",digit)
while num>0:
    r=num%10
    sum=sum+pow(r,digit)
    num=num//10
    print(r,'sum ',sum,' num ',num)
if tmp==sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong ")