places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
a=[]
i=len(places)-1
while i >0:
    places=places+[-i]
    a.append(places[i])
    i=i-1
print(a)

# i=2
# num=int(input("enter the number"))
# while i <num:
    # if num%i==0:
#         print(num,"is not prime number")
#         # i=i+1
#     else:
#         print(num, "is prime number")
#     i=i+1