# 1    -8   27  -64  .....    1000
i=1
cube=0
while cube<1000:
    cube=i*i*i
    if cube%2==0:
        cube=0-cube
        print(cube,end=" ")
        if cube==-1000:
            break
    else:
        print(cube,end="")
    i+=1