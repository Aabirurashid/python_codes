# Code likho jo iss list mein se maximum dhund kar ke print kare.
 
numbers = [50, 40, 23, 70,678, 56, 12, 5, 10, 7]
i=0
a=numbers[i]
while i <len(numbers):
    if a<numbers[i]:
        a=numbers[i]
    i=i+1
print(a)        

numbers = [50, 40, 23, 70,678, 56, 12, 5, 10, 7]
i=0
a=numbers[-1]
while i < len(numbers)-1:
    if a<numbers[-1]:
        a=numbers[i]
    i=i+1    
print(a)
numbers.remove(a)
i=0
l=numbers[-1]
while i<len(numbers)-1:
     if numbers[-1]>l:
          l=numbers[-1]
     i=i+1
print(l) 

           
