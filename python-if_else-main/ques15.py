num1=int(input("enter the first no:"))                                                                                                                                    
num2=int(input("enter the second no:"))
num3=int(input("enter the third no:"))

if num1<num2 and num3>num1:
    print(num1 ,"is smaller  ")
elif num2<num1 and num2<num3:
    print(num2, "is smaller")
elif num3<num1 and num2>num3:
    print(num3," is smaller")
else:
    print("not equal")

