n=int(input("enter the number of rows"))
for rows in range(n):
    for col in range(n):
        if col==0 or rows==(n-1) or rows==col:
            print("*",end=" ")
        else:
            print(end="  ")
    print( )
