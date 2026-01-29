#patter 4
'''
* * * * *
1
01
010
1010
10101
'''
    
for i in range(1,6):
    for j in range(1,i+1):
        if (i==2 or i==3):
            if(j%2==0):
                print('1',end='')
            else :
                print('0',end='')
        if(i==1 or i==4 or i==5):
            if(j%2!=0):
                print('1',end='')
            else :
                print('0',end='')
      
    print('')
    