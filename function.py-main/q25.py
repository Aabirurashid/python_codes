def multiply():
    sum=0
    for i in range(1,11):
        if not i%5 or not i%3:
            sum=sum+i
    print(sum)
multiply()
