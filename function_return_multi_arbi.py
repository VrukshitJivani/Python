def getArbi(*value):
    sum=0
    count=0
    for item in value:
        sum+=item
        count+=1
    avg=sum/count
    return sum,avg

result=getArbi(12,23,2,1,3,4,22)
print(result)