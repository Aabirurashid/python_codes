name=[ 'n', 't', 't', 'k', 'n' ] 
# name=(input("enter the name:"))
i=1
a=[]
while i<=len(name):
    a.append(name[-i])
    i=i+1
print(a)
if (name==a):
    print("palindrome")
else:
    print("not palindrome")
    



