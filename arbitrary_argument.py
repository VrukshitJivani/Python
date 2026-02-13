def getSum(*args):
    sum=0
    for i in args:
        print(i)
        sum+=i
    print(f"Sum of all numbers is: {sum}")
    
getSum(10,20,30,2,23,24,5,25,45)