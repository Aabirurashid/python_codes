n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
i=0
a=[]
while i<len(n):
    h=n[i]
    if h not in a:
        a.append(h)
    i=i+1
print(a)
# def function():
#     if speed<70:
#         print("ok")
#     elif speed>70:
#         a=speed-70
#         b=a//5
#         print(b,"points")
#         if b>=12:
#             print("lisense suspend")
# speed=int(input("enter the speed"))
# function()

    
