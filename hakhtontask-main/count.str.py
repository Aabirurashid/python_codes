# a='w3resource'
# count=0
# dic={}
# for i in a:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]=dic[i]+1
# print(dic)

# f='school'
# count=0
# dict={}
# for i in f:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]=dic[i]+1
# print(dict)

# c="Aabirrashid"
# count=0
# u={}
# for i in c:
#     if i not in u:
#         u[i]=1
#     else:
#         u[i]=u[i]+1
# print(u)

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