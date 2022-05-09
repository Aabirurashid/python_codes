a={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
d={}
for i in a:
    c=i*i
    d.update({i:c})
print(d)



import json


a={'lalalala': 3}

mystring = json.dumps(a)

print(mystring)


import json


dict1 ={

    "emp1": {

        "name": "Lisa",

        "designation": "programmer",

        "age": "34",

        "salary": "54000"

    },

    "emp2": {

        "name": "Elis",

        "designation": "Trainee",

        "age": "24",

        "salary": "40000"

    },

}
    