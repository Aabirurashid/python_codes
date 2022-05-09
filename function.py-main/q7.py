def calculator(number1,number2,operator):
    if operator=="+":
        return number1+number2
    elif operator=="-":
        return number1-number2
    elif operator=="*":
        return number1*number2
    elif operator=="/":
        return number1/number2
a=int(input("enter first number"))
b=int(input("enter second number"))
o=input("enter operator")
n=calculator(a,b,o)
print(n)
m=calculator(6,4,"-")
print(m)
b=calculator(6,4,"*")
print(b)
x=calculator(6,4,"/")
print(x)
print(n+5)


# Ek function likho jo ki ek argument le jo number ho or dictionary return karega jisme keys 1 se lekar argument ke number tak hogi aur values unke squares honge.jaisa ki niche dikhaya gaya hai.

# Input :- 20