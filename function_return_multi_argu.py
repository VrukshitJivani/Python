def getVal(no1,no2=0,no3=0):
    sum=no1+no2+no3
    square=no1*no1
    cub=square*no1
    return sum,square,cub    

result=getVal(10,20,30)
print(result)