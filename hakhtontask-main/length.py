# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# sum=0
# for d in student:
#     sum=sum+2
# print(sum)
# print(sum(d['id'] for d in student))
# print(sum(d['success'] for d in student))
# Write a Python program to convert a list into a nested dictionary of keys.
num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict) 
# = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for d_key, value in d.items():
#      print(d_key, 'corresponds to ', d[d_key]) 
# dict={"name":["aabiru","jabeen","saba"],
# "class":["11t

num_list=['a','b','i','r','u']
a=current={}
for  name in num_list:
    current[name]={}
    current=current[name]
print(a)
    
 

a
