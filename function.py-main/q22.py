def driver(speed):
    if speed<70:
        print("ok")
    elif speed>70:
        a=speed-70
        b=a//5
        print(b,"points")
        if b>=12: 
            print("lisence suspend")
n=int(input("enter the number"))
driver(n)
    

    