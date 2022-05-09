num=int(input("enter the number:"))
i=0
a=65
while i<=num:
    b=a
    j=1
    while j<=num:
        print(chr(a),end="")
        j=j+1
        a=a+1
    i=i+1
    print()