def getBin(no):
    if no>0:
        reminder=no%2
        no=no//2
        getBin(no)
        print(reminder,end=' ')

no=int(input("Enter number :"))
getBin(no)