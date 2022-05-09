# dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# sorted_values=sorted(dict.values())
# sorted_dict={}
# for i in sorted_values:
#     for k in dict.keys():
#         if dict[k]==i:
#             sorted_dict[k]=dict[k]
#             break
# print(sorted_dict)

dic={'aabiru':45,'karan':7,"jabeena":20,"param":34,"roshni":10}
sorted_values=sorted(dic.values())
sorted_dic={}
for i in sorted_values:
    for k in dic.keys():
        if dic[k]==i:
            sorted_dic[k]=dic[k]
            break
print(sorted_dic)