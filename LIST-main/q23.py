elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
a=[]
b=[]
sum=0
sum1=0
avg=0
while i<len(elements):
    j=elements[i]
    if j%2==0:
        a.append(j)
        sum=sum+j
    else:
        b.append(j)
        sum1=sum+j
    i=i+1
avg=sum/4
avg=sum1/7
print("average is ",avg)