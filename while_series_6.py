#0    1   1   2   3   5   8   13  .... 100
first=1
second=1
ans=0
i=1
num=int(input("Enter number :"))
print("0 1 1",end=" ")
while i<num-2:
    ans=first+second
    print(ans,end=" ")
    first=second
    second=ans
    i+=1
    