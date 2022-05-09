import requests
import json
get_url=requests.get("https://api.merakilearn.org/courses")
meraki_learn=get_url.json()
with open("folder.json","w")as file_data:
    file=json.dump(meraki_learn,file_data,indent=4)
serial_number=1
for i in meraki_learn:
    print(serial_number,".",i["name"],":",i["id"])
    serial_number+=1
course_no=int(input("enter ur number do u want:"))
print(meraki_learn[course_no-1]["name"])
idd=meraki_learn[course_no-1]["id"]
m1=input("what do u want pervious or next(n/p):")
if m1=="p":
    serial_number=1
    for i in meraki_learn:
        print(serial_number,".",i["name"],":",i["id"])
        serial_number+=1
    course_no=int(input("enter ur number do u want:"))
    print(meraki_learn[course_no-1]["name"])
    idd=meraki_learn[course_no-1]["id"]
elif m1=='n':
    url=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
    var=url.json()
    with open("topic.json","w")as k:
        json.dump(var,k,indent=4)
        serial_number2=1
        list1=[]
        list2=[]
    for j in var["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_number2,".",j["name"])
            print("      ",serial_number2,".",j["slug"])
            serial_number2+=1
            new_no=1
            list1.append(j)
            list2.append(j)
    for j in var["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_number2,".",j["name"])
            print("    ",serial_number2,".",j["slug"])
            serial_number2+=1
            new_no=1
            list1.append(j)
            list2.append(j)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial_number2,".",j["name"])
        serial_number2+=1
        new_no=1 
        list1.append(j)
    for l in var["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print("     ",new_no,j["name"])
            new_no+=1
            list2.append(j)
            break
m1=input("what do u want pervious or next(n/p):")
if m1=="p":
    serial_number=1
    for i in meraki_learn:
        print(serial_number,".",i["name"],":",i["id"])
        serial_number+=1
    course_no=int(input("enter ur number do u want:"))
    print(meraki_learn[course_no-1]["name"])
    idd=meraki_learn[course_no-1]["id"]
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
        point=int(input("enter the number point:"))
        for k in list1:
            if k["parent_exercise_id"]==k["id"]:
                print(list1[point-1]["name"])
                num=(list1[point-1]["id"])
                var=[]
                var3=[]
                new_no1=1
                for n in list2:
                    if n["parent_exercise_id"]==num:
                        print("  ",new_no1,n["name"])
                        var.append(n["name"])
                        var3.append(n["content"])
                    new_no1+=1
                point1=int(input("enter the point1 do u want:"))
                new_no2=1
                for s in range(0,len(var)):
                    if point1==new_no2:
                        print(var[s])
                        print(var3[s])
                    new_no2+=1
        