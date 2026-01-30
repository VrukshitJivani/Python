def getSquer(nom):
    squer=nom*nom
    return squer
    
def getQube(num):
    qube=getSquer(num)*num
    return qube

no=int(input("Enter number "))
s=getSquer(no)
q=getQube(no)
print('squar is :',s)
print('qube is :',q)