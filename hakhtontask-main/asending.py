
# dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values=sorted(dict.values())
# sorted_dict={}
# for i in sorted_values:
#     for k in dict.keys():
#         if dict[k]==i:
#             sorted_dict[k]=dict[k]
#             break
# print(sorted_dict)


num=int(input("enter the number"))
i=0
while i<num:
    print("---"*num)
    print(f"|{0}"*num+"|")
    i=i+1
if i==num:
    print("---"*num)    



