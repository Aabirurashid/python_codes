# city_population = {

#     "NewYorkCity":8550405,

#     "LosAngeles":3971883, 

#     "Toronto":2731571, 

#     "Chicago":2720546, 

#     "Houston":2296224, 

#     "Montreal":1704694, 

#     "Calgary":1239220, 

#     "Vancouver":631486, 

#     "Boston":667137

# }


# print(city_population["NewYorkCity"])

# print(city_population)

# print(type(city_population))

# student=dict(name= "Ravina",age= 20)
# print(student)


# my_dict = {

#     1: 'apple', 

#     2: 'ball'

# }

# Dic= {

#  1: 'NAVGURUKUL',

#  2: 'IN',  

#  3:{

#      'A' : 'WELCOME',

#      'B' : 'To', 

#      'C' : 'DHARAMSALA'

#      }

# }

# print(Dic)


# person={

#     'name':'jack',

#     'age':20,

#     'gender':'male',

#     4:'organisation'}


# result = person['age'] 

# x = person.get("gender")

# print(person[4])

# print(x)

# print(result)


# person={

#     'name':'jack',

#     'age':20,

#     'gender':'male',

#     4:{

#         'organisation':'navgurukul','place':'dharamsala'

#         }

#     }

# print(person['gender'])


# print(person[4])


# result = person[4]['place']


# print(result)

# dic= {

#    'Name': 'RAM',

#    'Age': 17,

#     }

# dic['student']={

#        'id':22, 

#        'place':'dharamsala'

#    }

# print(dic)

# car ={

#     "brand":  "ford",

#     "model":  "mustang",

#     "year":  1964

# }

# if "model" in car:

#     print("Yes, 'model' is one of the keys in the car dictionary.")


# else:

#     print("No, 'model' key dictionary mai nahi hai.")

# person= {'1': 'RAM', '2': 17,}

# person[3] = 'male'

# print(person)

# details={

#     'Name': 'RAM',

#      'Age': 17, 

#      'student': {

#       'id': 22,

#       'place': 'dharamsala'

#       }

#      } 

# details['student']['id']=35

# print(details); 

# dic///////
# dict1["color"]="white"
# print(dict1)
# x=dict1["model"]
# print(x)
# y=dict1.get("model")
# print(y)
# # z=dict1["year"]
# # print(z)
# for x,y in dict1.items():
#     print(x,y)

# x=('firstkey','secoundkey','thirdkey')
# y=0
# dict1=dict.fromkeys(x,y)
# print(dict1)

# dict1={'brand':'suzuki','model':'dezire','year':2020}
# dict1.update({"colour":"white"})
# print(dict1)

# Dict = {

#        'ball' : 'green',

#        'Ball': 'red'

#      }

# print(Dict['ball'])

# print(Dict['Ball'])

# print(Dict['bat'])

# details ={

#     "name":  "Bijender",

#     "age":  17,

#     "class":  "10th"

#     }

# for x in details.values():

#     print(x)

# a = {(1,2):1,(2,3):2}

# print(a[1,2])

# a= {'a':1,'b':2,'c':3}
# print (a['a','b'])

# fruit = {}


# def addone(index):

#     if index in fruit:

#         fruit[index] += 1

#     else:

#         fruit[index] = 1

        

# addone('Apple')

# addone('Banana')

# addone('apple')

# addone('Apple')


# print (len(fruit))

# print(fruit)

# Student = {}

# Age = {}

# Details = {}

# Student['name'] = "bikki"

# Age['student_age'] = 14

# Details['Student'] = Student

# Details['Age'] = Age


# print (len(Details["Student"])) 


# my_dict = {}

# my_dict[(1,2,4)] = 8

# my_dict[(4,2,1)] = 10

# my_dict[(1,2)] = 12


# sum = 0

# for k in my_dict:

#     sum += my_dict[k]


# print (sum)

# print(my_dict)

# box = {}

# # jars = {}

# # crates = {}

# # box['biscuit'] = 1

# # box['cake'] = 3

# # jars['jam'] = 4

# # crates['box'] = box

# # crates['jars'] = jars

# # print (len(crates['box']))


# rec = {

# "Name" : "Python", 

# "Age":"20",

# "Addr" : "NJ", 

# "Country" :"USA"

# }

# id1 = id(rec)

# del rec


# rec = {

#     "Name" : "Python", 

#     "Age":"20", 

#     "Addr" : "NJ", 

#     "Country" : "USA"

#     }

# id2 = id(rec)

# print(id1 == id2)

# details={

#     "name":"Shanti",

#     "age":12,

#     "email":"shanti@navgurukul.org",

#     }


# print(details["name"])

# print(details["email"])

# print(details['age'])

# dict1={1:2,2:3,3:4,4:5}

# sum=0

# for i in dict1.values():    
#     sum=sum+i
# print(sum)
# c=dict()
# a={}
# for i in range(1,16):
    # a.update({c[i]:c[i]**i})
    # c=i*i
    # print(a) 


# a={}
# for i in range(0,len(numbers)):
#     a.update({numbers[i]:numbers[i]**2})
# print(a)
    

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}

# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)


# import json


# dict1 ={

#     "emp1": {

#         "name": "Lisa",

#         "designation": "programmer",

#         "age": "34",

#         "salary": "54000"

#     },

#     "emp2": {

#         "name": "Elis",

#         "designation": "Trainee",

#         "age": "24",

#         "salary": "40000"

#     },

# }
# out_file = open("myfile.json", "w")


# json.dump(dict1, out_file, indent = 6)


# out_file.close()

# import json


# a={'lalalala': 3}

# mystring = json.dumps(a)

# print(mystring)


# import json

# dict1={
#     "Name":"Ram", 
#      "Class":"IV", 
#      "Age":9 

# }
# in_file= open("dict.json","w")
# json.dump(dict1,in_file,indent=6)
# in_file.close()


# for i in range(5):
#     print(i)

# for i in (4,3,2,1,0):
#     print(i)

# for i in range(10):
#     if(i%2!=0):
#         print("Hello",i)



# import pandas as pd
# import numpy as np

# d = {"name":'name',"empno":1}
# d1 ={"name":'name1',"empno":2}
# d2 ={"name":'name2',"empno":3}
# d3 ={"name":'name3',"empno":4}
# s = pd.DataFrame([d,d1,d2,d3])
# print(s)

# import json
# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 6  
# }
# print(type(python_obj))
# j_data = json.dumps(python_obj)
# print(j_data)

# Original String:
# {'4': 5, '6': 7, '1': 3, '2': 4}

# JSON data:
# {
#     "1": 3,
#     "2": 4,
#     "4": 5,
#     "6": 7
# }


# name="nikita"
# count=0
# y={}
# for i in name:
#     if i not in y:
#         y[i]=1
#     else:
#         y[i]=y[i]+1
# print(y)


