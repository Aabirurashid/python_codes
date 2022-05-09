import json
list1=["neelam","programer","24","2400"]
keys1={"name","designation","age","salery"}
emp1={}
for keys in keys1:
    for values in list1:
        emp1[keys]=values
        list1.remove(values)
        break
list2=["komal","trainer","24","20000"]
keys1={"name","designation","age","salery"}
emp2={}
for keys in keys1:
    for values in list2:
        emp2[keys]=values
        list2.remove(values)
        break
list3=["anuradha","HR","25","40000"]
keys1={"name","designation","age","salery"}
emp3={}
for keys in keys1:
    for values in list3:
        emp3[keys]=values
        list3.remove(values)
        break
list4=["Abhishek","manager","29","63000"]
keys1={"name","designation","age","salery"}
emp4={}
for keys in keys1:
    for values in list4:
        emp4[keys]=values
        list4.remove(values)
        break
dict1={}
dict1.update({"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4})
# print(dict1)
# with open("salery.json","w")as json_file:
    # json.dump(dict1,json_file,indent=3)

           

    





