# number=[50, 40, 23,22,24,33, 70, 56, 12, 5, 10, 7]
# length=len(number)
# a=[]
# for i in range(length):
#     if number[i]>20 and number[i]<40:
#         a.append(number[i])
# print(a)



number=[50, 40, 23,22,24,33, 70, 56, 12, 5, 10, 7]
a=[]
i=0
while i< len(number):
    if number[i]>20 and number[i]<40:
        j=number[i]
        a.append(j)
    i=i+1
print(a)


# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# a=[]
# while i<len(n):
#     j=len(n)-1
#     while j>4:
#         if n[i]+n[j]==number:
#             a.append([n[j],n[i]])
#         j=j-1
#     i=i+1
# print(a)


number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
a=[]
while i<len(n):
    j=len(n)-1
    while j>4:
        if n[i]+n[j]==number:
            a.append([n[i],n[j]])
        j=j-1
    i=i+1
print(a)











