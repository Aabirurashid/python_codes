i=int(input("enter the number"))
orignal=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if sum==orignal:
    print("amstrong number")
else:
    print("not amstrong number")
