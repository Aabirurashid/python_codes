

marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65, 76],

    [95, 45, 78, 52, 49]

]

i=0
sum=0
while i<len(marks):
    j=0
    a=0
    while j<len(marks[i]):
        a=a+marks[i][j]
        j=j+1 

    sum=sum+a
    i=i+1
print(sum)

# question2
marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65],

    [95, 45, 78]

]
i=0
sum=0
while i<len(marks):
    j=0
    g=0
    while j<len(marks[i]):
        g=g+marks[i][j]
        j=j+1
    sum=sum+g
    i=i+1
print(sum)



#question3
marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65],

    [95, 45, 78],

    [87, 67, 49, 68, 88]

]
i=0
sum=0
while i<len(marks):
    j=0
    a=0
    avg=0
    while j<len(marks[i]):
        a=a+marks[i][j]
        j=j+1
    sum=sum+a
    i=i+1
    avg=sum/17
print(sum)
print(avg)
