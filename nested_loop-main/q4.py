i=1
while i<=5:
    j=1
    while j<=7:
        if i+j==5 or j-i==3  or i==4:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    print( )
    i=i+1