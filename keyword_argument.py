def getMarksum(computer,math,science,english):
    sum=computer+math+science+english
    return sum
    
e=int(input('Enter english marks :'))
m=int(input('Enter math marks :'))
s=int(input('Enter science marks :'))
c=int(input('Enter computer marks :'))
result=getMarksum(english=e,math=m,science=s,computer=c)
print(result)