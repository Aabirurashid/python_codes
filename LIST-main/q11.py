elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# a=[]
# # size=int(input("enter the number"))
# for i in range(size):
#     val=int(input("enter the number"))
#     a.append(val)
# even=0
# odd=0
# for i in range(size):
#     if(a[i]%2==0):1
#         even=even+1
#     else:
#         odd=odd+1
# print("Total Even=",even,"Total Odd=",odd)




# even=0
# odd=0
# i=0
# while i<len(elements):
#     if (elements[i]%2==0):
#         even=even+1
#     else:
#         odd=odd+1
#     i=i+1
# print("Totol Even=",even,"Total Odd=",odd)

a=[[4,5,6],8,[9,10,11],12]
i=0
even=0
odd=0
while i<len(a):
    b=a[i]
    if type(b)is list:
        for j in range(len(b)):
            if b[i]%2==0:
                even=even+1
            else:
                odd=odd+1
    else:
        a[i]%2==0
    i=i+1
print("Total Even=",even,"Total Odd=",odd)
