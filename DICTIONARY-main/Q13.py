my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in my_dict:
    a.append(my_dict[i])
max=0
b=[]
x=0
while x<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    x=x+1
y=1
while y<=3:
    b.append(a[-y])
    y=y+1
print(b)

    # if my_dict[i]>max:
    #     max=my_dict[i]
    
    # print(max)