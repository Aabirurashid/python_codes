import requests
import json
get_url=requests.get("https://api.merakilearn.org/courses")
meraki_learn=get_url.json()
with open("Aabiru.json","w") as file_data:
    file=json.dump(meraki_learn,file_data,indent=4)
serial_no1=1
for i in meraki_learn:
    print(serial_no1,".",i["name"],":",i["id"])
    serial_no1+=1
course=int(input("enter the serial number:"))
print(meraki_learn[course-1]["name"])
id=meraki_learn[course-1]["id"]
nev1=input("what do u want **next**   or**previous(p/n):")
if nev1=="p":
    serial_no1=1
    for i in meraki_learn:
        print(serial_no1,".",i["name"],":",i["id"])
        serial_no1+=1
    course=int(input("enter the serial number:"))
    print(meraki_learn[course-1]["name"])
    id=meraki_learn[course-1]["id"]
elif nev1=="n":
    url=requests.get("http://api.merakilearn.org/courses/"+str(id)+"/exercise")
    var=url.json()
    with open("moomin.json","w") as k:
        json.dump(var,k,indent=4)
        serial_no2=1
        list1=[]
        list2=[]
        for j in var["courses"]["exercises"]:
            if j["parent_exercise_id"]==None:
                print(serial_no2,".",j["name"])
                print("     ",".",serial_no2,j["slug"])
                serial_no2+=1
                new_no=1
                list1.append[j]
                list2.append[j]







