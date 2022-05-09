def perfect():
    i=1
    while i<10:
        j=1
        f=0
        sum=0
        while i>j:
            if i%j==0:
                sum=sum+j
                f=f+1
                # print(j)
                # print(sum,"sum")
        
            j+=1
        if f==2:
            print(j,"it is perfect no")
        i+=1
perfect()
i=1
k=1
while i<=5:
    b=1
    while b<=5-i:
        print('_',end="")
        b=b+1
    j=1
    while j<=k:
        print("*",end='')
        j=j+1
    k=k+2
    print()
    i=i+1
    