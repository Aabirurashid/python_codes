import json
def  get_list_details():
    file1=open("file1.json","r")
    y=json.load(file1)
    # print(y)
    list3=[]
    for i in y:
        # print(y)
        # print(i["Original Language"])
        if i["Original Language"]not in list3:
            list3.append(i["Original Language"])
            # print(p)
    dict2={}
    list5=[]
    for k in list3:
        i=0
        count=0
        while i<len(y):
            if k==y[i]["Original Language"]:
                count+=1
            i+=1
        dict2.update({k:count})
    list5.append(dict2)
    with open("mehak.json","w")as file:
        json.dump(dict2,file,indent=4)
    return dict2
get_list_details()

