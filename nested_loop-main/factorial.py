n=int(input("enter the factor"))
factor=2
while factor<=n/2:
    if n%2==0:
        print(factor,end=' ')
    factor+=1
print(n,end=' ')
