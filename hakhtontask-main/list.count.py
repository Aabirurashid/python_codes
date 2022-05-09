char_list="MISSISSIPPI"
i=0
d=[]
while i<len(char_list):
    j=0
    b=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    b.append(char_list[i])
    b.append(count)
    if b not in d:
        d.append(b)
    i=i+1
print(d)