number=[1,28,90,81,51,70,4,0]
i=0
a=number[0]
while i<len(number):
    if number[i]<a:
        a=number[i]
    i=i+1
print(a)
number.remove(a)
j=0
b=number[0]
while j<len(number):
    if number[j]<b:
        b=number[j]
    j=j+1
print(b)
number.remove(b)
c=0
s=number[0]
while c<len(number):
    if number[c]<s:
        s=number[c]
    c+=1
print(s)

