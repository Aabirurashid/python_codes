d =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count = 0
for x in d:
        count += len(d[x])
print(count)
