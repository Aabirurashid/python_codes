def add_numbers(num1,num2):

    num1 = 56

    num2 = 12
    print(num1+num2)

add_numbers(50,12)


def add_numbers_list(a,b):
    i=0
    sum=0
    # mul=0
    while i<len(a):
        sum=a[i]+b[i]
        print(sum)
        i+=1
add_numbers_list([50,60,10],[10,20,13])