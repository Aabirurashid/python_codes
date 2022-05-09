num1=int(input("enter the first number"))
num2=int(input("enter the secound number"))
num3=int(input("enter the 3rd number"))
if num1>num2 and num3<num1:
    print(num1,"is greater number")
elif num2>num1 and num2>num3:
    print(num2,"is greater number")
elif num3>num1 and num3>num2:
    print(num3," is greater number")
else:
    print("not equal")