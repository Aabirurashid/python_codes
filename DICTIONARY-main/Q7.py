a=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
i=0
t={}
c=[]
while i<len(a):
     t.update(a[i])
     i=i+1
for i in t.values():
     if i not in c:
          c.append(i)
print(c)
