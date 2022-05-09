n=int(input("enter the number"))
i=1
while i<=5 :
    j=1
    while j<=i:
        if j==1 or i==j or i==5:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    print( )
    i=i+1