# code likho jo iss list mein se second maximum element (doosra sabse bada element) dhund kar kar print kare.
 
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
a=numbers[1]
while i<len(numbers):
     if numbers[i]>a:
         a=numbers[i]   
     i=i+1
numbers.remove(a)
i=0
l=numbers[i]
while i<len(numbers):
     if numbers[i]>l:
          l=numbers[i]
     i=i+1
print(l) 



