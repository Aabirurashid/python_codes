dict1={1:10, 2:20}
dict2={3:30,2:40}
dict3={5:50,6:60}
for key in dict1:
    if key in dict2:
        dict2[key]=dict1[key]+dict2[key]
        dict2.update(dict3)
    else:
        dict2[key]=dict1[key]
print(dict2)