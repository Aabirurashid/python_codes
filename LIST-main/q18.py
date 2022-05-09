a=[5,8,7,9,22,66,99,120]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
print("before:",a)
i=1
c=[]
while i<=len(a):
    c.append(a[-i])
    i=i+1
print("now:",c)