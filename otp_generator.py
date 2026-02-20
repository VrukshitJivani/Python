import random

i=0
list=[]
while i<=5:
    list.append(str(random.randint(0,9)))
    i=i+1
otp=''.join(list)
print(otp)
