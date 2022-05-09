y=open("people1-exercise.txt","r")
for i in y:
    if "delhi"in i:
        y=open("delhi.txt","a")
        y.write(i)
    elif "shimla" in i:
        y=open("shimla.txt","a")
        y.write(i)
    else:
        y=open("others.txt","a")
        y.write(i)
y.close()


 
