a=[1,2,3,4,5,6,8]
d=[]
i=len(a)-1
while i>=0:
    a=a+[-i]
    d.append(a[i])
    i=i-1
print(d)