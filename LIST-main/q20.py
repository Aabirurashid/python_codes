mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on" 
l=mainStr.split()
i=0
while i<len(l):
    if l[i]=="over":
        x=mainStr.replace("over","on")
    i=i+1
print(x)
