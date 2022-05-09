def check_numbers(a,b):
    if (a%2==0 and b%2==0):
        print("even numbers hai")
    else:
        print("dono numbers even nhi hai")

check_numbers(7,9)

def check_numbers(a,):
    # a=[2, 6, 18, 10, 3, 75] 
    # b=[6, 19, 24, 12, 3, 87]
    for i in range(0,len(a)):
        if a[i]%2==0:
            print("even")
        else:
            print("odd")
check_numbers([2, 6, 18, 10, 3, 75] )
check_numbers([6, 19, 24, 12, 3, 87])