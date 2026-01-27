#write a program to figure out whether given number  is composite number or not
#4 → factors: 1, 2, 4 → ✅ composite -it factore is more than 2
import sys
i=2
flage=0
num=int(input('Enter number :'))
half=(num//2)+1
if num<=1:
    print("Number is not composite ")
    sys.exit(0)
while i<half:
    if num%i==0:
       flage+=1
    i+=1
print(flage)
if flage>0:
    print("Number is composite ")
else:
    print("Number is not composite ")