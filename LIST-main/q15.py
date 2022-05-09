# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ] 
# i=0
# sum=0
# a=[]
# while i<len(magic_square):
#     j=magic_square[i]
#     if j:
#         a.append(i)
#         sum=sum+1
#     i=i+1
#     # a=a+1
# print(sum)



#  /Python3 code to demonstrate
# shuffle a list
# using Fisher–Yates shuffle Algorithm
 
import random
 
# initializing list
test_list = [1, 4, 5, 6, 3]
 
# Printing original list
print ("The original list is : " + str(test_list))
 
# using Fisher–Yates shuffle Algorithm
# to shuffle a list
for i in range(len(test_list)-1, 0, -1):
     
    # Pick a random index from 0 to i
    j = random.randint(0, i + 1)
   
    # Swap arr[i] with the element at random index
    test_list[i], test_list[j] = test_list[j], test_list[i]
     
# Printing shuffled list
print ("The shuffled list is : " +  str(test_list))