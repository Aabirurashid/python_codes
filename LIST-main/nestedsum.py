a=[[4,5,6],8,[9,10,11],12]

for i in range(len(a)):
    b=a[i]
    if type(b)is list:
        for j in range(len(b)):
            c=b[j]
            if c%2==0:
                print(c,"even")
            else:
                print(c,"odd")
    else:
         if b%2==0:
            print(b,"even")
         else:
             print(b,"odd")







# def change_sring(str1):
#       return str1[-1:] + str1[1:-1] + str1[:1]
	  
# print(change_sring('abcd'))
# print(change_sring('12345'))
# list=input("enter the str: ")
# counter=0
# for i in list:
#     counter+=1
# print(counter)a=[[4,5,6],8,[9,10,11],12]

for i in range(len(a)):
    b=a[i]
    if type(b)is list:
        for j in range(len(b)):
            c=b[j]
            if c%2==0:
                print(c,"even")
            else:
                print(c,"odd")
    else:
         if b%2==0:
            print(b,"even")
         else:
             print(b,"odd")



# n = int(input("Input a number: "))

# # use for loop to iterate 10 times
# for i in range(1,11):
#    print(n,"x",i,'=',n*i)
