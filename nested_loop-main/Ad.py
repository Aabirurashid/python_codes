a=[10,20,30,40,50]
b=[100,200,300,400,500]
i=0
j=-1
while i < len(a):
    list1= a[i]
    list2= b[::j][i]
    i+=1
    print(list1,list2)