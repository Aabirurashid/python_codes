def namefunction(a,b):
    a=input("enter the name:")
    b=input("enter the name:")
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    elif len(a)==len(b):
        print(a)
        print(b)
    else:
        ("invalid")

namefunction("aabiru","neha")
