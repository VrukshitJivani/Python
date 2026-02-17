def getNum(a):
    if a>=1:
        print(a,end=' ')
        a-=1
        getNum(a)

number=10
getNum(10)
