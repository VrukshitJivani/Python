#no return value,no arguments 
def getSquer():
    nom=4
    squer=nom*nom
    print('squar is :',squer)
    
#no return value,with arguments 
def getQube(num):
    qube=num*num*num
    print('qube is :',qube)

# return value,no arguments 
def getSum():
    sum=10+20
    return sum
 # return value,no arguments 
def getMulti(a,b):
    multiplication=a*b
    return multiplication 
       
no1=21
no2=2

getSquer()

getQube(no1)

sum=getSum()
print("sum is ",sum)

multiply=getMulti(no1,no2)
print("Multiplication is ",multiply)

