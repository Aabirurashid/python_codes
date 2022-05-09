a = [1,2,3,4,5,6]
b = [2,3,1,0,6,7] 
j=[]
i=0
while i<len(a):
    k=a[i]
    if k not in b:       
     j.append(k)
    i=i+1
print(j)
