my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in my_dict.keys():
    if my_dict[i]>50:
        a.append(i)
print(a)


s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}

a={'python':20,"gaurav":300,'dev':34,"karan":43}

c={}

for i in (s,a):

    c.update(i)

print(c)