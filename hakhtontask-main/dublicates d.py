# my_dict={}
# if not bool(my_dict):
#     print("dictionary is empty")

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)

#  num=int(input("enter the number"))







