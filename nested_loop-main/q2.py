i=1
while i<=7:
    j=6
    while j>=i:
        if i==1 or j==6 or i==j:
            print("*",end="")
        else:
            print(" ",end="")
        j=j-1
    print( )
    i=i+1