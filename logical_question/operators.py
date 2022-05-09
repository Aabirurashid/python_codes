# x = 5.2
# if (type(x) is not int): 
#     print("true") 
# else: 
#     print("false") 

# x = 10
# y = 50
# if (x ** 2 > 100 and y < 100):
#     print(x)

# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)

# alphabet=input("enter the alphabet:")
# a="asdfghjklqwertyuiopzxcvbnm"
# if alphabet in a:
#     print("it is alphapet")
# else:
#     print("not alphabet")
# var=input("enter the alphabet:")
# a="aeiouAEIOU"
# if var in a:
#     print("it is vowel")
# else:
#     print("consonent")

# i=1
# while i<10:
#     c=i**2
#     print(i,c)
#     i=i+1

# i=10
# while i<=300:
#     print(i)
#     i=i+10

# i=105
# while i>=7:
#     print(i)
#     i=i-7

# num=int(input("enter the number"))
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# print(rev)


# a=[1,2,3,4,5,6,8]
# d=[]
# i=len(a)-1
# while i>=0:
#     a=a+[-i]
#     d.append(a[i])
#     i=i-1
# print(d)

# i=0
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)

# i=0
# sum=0
# while i<=20:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print(sum)

# a=5
# b=5
# if a is not b:
#     print("true")
# else:
#     print("false")

# i=1
# while i<=5:
#     j=0
#     while j<=5:
#         print(i,end="")
#         j=j+1
#     i=i+1
#     print()

# a=[1,2,3,[3,4],[7,8],5,7]
# i=0
# b=[]
# for i in a:
#     if type(a[i]) is list:
#         c=a[i]
#         for j in c:
#             print(c[j])
# print(b)
# :
    # for i in l:
    #     if type(i) == list:
    #         reemovNestings(i)
    #     else:
    #         output.append(i)
  
# Driver code
# print ('The original list: ', l)
# reemovNestings(l)
# print ('The list after removing nesting: ', o

# for i in (1,2,3):
#     print(i)

# for i in (4,3,2,1,0):
#     print(i, end=" ")
# str = "Python Output based Questions"
# word=str.split()
# for i in word:
#     print(i)

# for i in range(7,-2,-9):
#     for j in range(i):
#         print(j)
# i="9"
# for k in i:

    # print(k)

# for i in range(1,8):
#     print(i)
#     i+=2

# for i in range(5):
    # while(i):
    #     print(i,end=" ")

# for i in range(7):
#     while(i):
#         print(i,end=" ")
#         i=i-1
#     print()

# x=5
# while(x<15):
#   print(x**2)
#   x+=3                                                                                         
# b=5
# while(b<9):
#   print("H")
#   b+=1


# b=15
# while(b>9):
#   print("Hello")
#   b=b-2 

# for i in range(5):
#     for j in range(i):
#         print("A",end=" ")
#     print()

# for i in range(5):
#     for j in range(i):
#         print("A",end="a")
#     print()

# s1="csworld.com"
# s2=""
# s3=""
# for x in s1:
#      if(x=="s" or x=="n" or x=="p"):
#            s2+=x
# print(s2,end=" ")
# print(s3)
# j=12
# c=9
# while( j):
#      if( j>5):
#            c=c+j-2
#            j=j-1
#      else:
#           break
# print(j, c)
# print(c)
# L = [13 , 12 , 21 , 16 , 35 , 7, 4]
# s = 5
# s1 = 3
# for i in L:
#      if (i % 4 == 0):
#           s = s + i
#           continue
#      if (i % 7 == 0):
#           s1 = s1 + i
# print(s , end=" ")
# print(s1)
# def fib(n):
#     p, q = 0, 1
#     while(p < n):
#         yield p
#         p, q = q, p + q

# x = fib(10)

# grocery_list = ['flour','cheese','carrots']
# i=0
# while i<len(grocery_list):
#     print(i,grocery_list[i])
#     i=i+1
# a= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# sum=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     i+=1
# print(sum)
# List = [1,2,3,1,2,2]
# i=0
# a=[]
# while i<len(List):
#     c=List[i]
#     if c not in a:
#         a.append(c)
# print(a)


# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
# check2 = check1
# check3 = check1[:]
 
# check2[0] = 'Code'
# check3[1] = 'Mcq'
 
# count = 0
# for c in (check1, check2, check3):
#     if c[0] == 'Code':
#         count += 1
#     if c[1] == 'Mcq':
#         count += 10
 
# print (count)

# a=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
 
# for i in a:
#     if i%2==0:
#         print(i,end=' ')

# list1 = [4, 6, 8, 24, 12,2]
# list1 = [4, 6, 8, 24, 12,2]
# min= sorted(list)
# print(min)

# d1={'a':100,'b':200,'c':300}
# d2={'a':300,'b':200,'d':400}
# d3={}
# for key in d1:
#     if key in d2:
#         d3[key]=d1[key]+d2[key]
#         d2.update(d3)
#     else:
#         d2[key]=d1[key]
# print(d2)


# a=[1,2,3,4,5]
# i=0
# while i<len(a)-1:
#     b=a[i+1]-a[i]
#     print(b)
#     i=i+1

# a={"Aabiru":"abiru","Aabiru":"abiru"}
# b={}
# for x,y in a.items():
#     b[y]=x
# print(b)


# char_list="MISSISSIPPI"
# i=0
# d=[]
# while i<len(char_list):
#     j=0
#     b=[]
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count=count+1
#         j=j+1
#     b.append(char_list[i])
#     b.append(count)
#     if b not in d:
#         d.append(b)
#     i=i+1
# print(d)

# b=[1,2,3,4,5,6,7,8,9,10,11,12,16]
# i=1
# c=20
# while i<len(b):
#     b.insert(i,c)
#     i+=3+1
# print(b)

# a=[1,6,7,8,9,3,4,5,12,13]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
#         j=j+1
#     i=i+1
# print(a)
    
# num=int(input("enter the number:"))
# a=num%10
# b=(num//10)%10
# c=(num//100)%10
# d=(num//1000)%10
# e=(a*1000)+(b*100)+(c*10)+(d*1)
# print(e)
# if num==e:
#     print(a)




a=[65,[7,8,9],[4,1,9,3],67]
i=0
sum=0
while i<len(a):
    b=a[i]
    if type(b) is list:
        for j in range(len(b)):
            sum=sum+b[j]
            # j+=1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)

# a=[1,2,3,4,5,6,7,8,9,10]
# i=1
# n=[]
# while i<len(a)+1:
#     n.append(a[-i])
#     i+=1
# print(n)
# a=[1,2,3,4,5,6,7]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# n=int(input("enter the number:"))
# i=1
# s=0
# while i<n:
#     if n%i==0:
#         s=s+i
#     i=i+1
# if s==n:
#     print("perfect number")
# else:
#     print("not perfect number")


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i=i+1
# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1
# i=0
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

# i=0
# while i<=5:
#     j=5
#     while j>=i:
#         print("*",end="")
#         j-=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1
# a=5
# b=float(a)
# c=str(b)
# print(type(b),type(c))

# a=int(input("enter the ist number:"))
# b=int(input("enter the 2nd number:"))
# c=int(input("enter the 3rd number:"))
# if a>b and a<c:
#     print(a,"")
# elif b<c:
#     print(b,"its")
# else:
#     print(c,"lkjh")
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

    # print("*"*i)
    # i+=1

# num=int(input("enter the number:"))
# sum=0
# i=0
# temp=num
# while temp>0:
#     i=temp%10
#     sum=sum+i**3
#     temp=temp//10
# if num==sum:
#     print(num,"amstrong number")
# else:
#     print("not amstrong number")     

# num=int(input("enter the number:"))
# if num>0:
#     print(num,"x","="*1)
    # print(num*2)
    # print(num*3)
    # print(num*4)
    # print(num*5)
    # print(num*6)
    # print(num*7)
    # print(num*8)
    # print(num*9)
#     # print(num*10)
# else:
#     print("nothing")

# i=1
# while i<=5:
#     print("*"*i)

# var myResult= 2+3;

# console.log(myResult);
# var num1;

# num1 = 6;

# var num2
# i=5
# while i>=1:
#     j=1
#     if j<=5:
#         print(i,i,i,i,end="")
#         j=j+1
#     print()
#     i=i-1

# i=5
# while i>=1:
#     print(str(i)*5)
#     i=i-1

# num=int(input("enter the number:"))
# i=1
# a=num
# while i<=num:
#     j=1
#     while j<=5:
#         print(a,end="")
#         j=j+1
#     i=i+1
#     a=a-1
#     print()

# name=[ 'n', 'i', 't', 'i', 'n', ] 
# # name=(input("enter the name"))
# # a=[]
# i=1
# while i<=len(name)-1:
#     a=(name[-i])
#     i=i+1
# # print(a)
# if (a==name):
#     print("palindrome")
# else:
#     print("not palindrome")
# a=[121,"abc","acd"]

# a=["python",30,4.6,True]
# i=0
# while i<len(a):
#     if type(a[i])==bool:
#         print(a[i])
#     i=i+1


# from tkinter import*
# from random import randint  
# from tkinter import ttk

# root=Tk()
# root.title("my window name")
# label=Label(root,font=("Arial",21),text="game of rock,paper,scissoir",bg="black",fg="white")
# label.pack()
# root.geometry("800x900+300+200")
# root.resizable(0,0)
# # root.mainloop()

# rock=PhotoImage(file="/home/anushka/Downloads/ocks.pngr")
# paper=PhotoImage(file="/home/anushka/Downloads/papers.png")
# scissoir=PhotoImage(file="/home/anushka/Downloads/scissorss.png")
# var = StringVar()
# image_list=[rock,paper,scissoir]
# pick_number=randint(0,2)

# image_label=Label(root,image=image_list[pick_number])
# image_label.pack(pady=20)

# #create spin function

# def spin():
#     pick_number=randint(0,2)
#     image_label.config(image=image_list[pick_number])
#     def win():
#         print("you win!")

#     def lose():
#         print("you loss!")
#     while True:
#         player_choice=input("what do you pick?(rock,paper,scissors)")
#         player_choice.strip()
#         random_moves=randint(0,2)
#         moves=["rock","paper","scissors"]
#         computer_choice=moves[random_moves]
#         print(computer_choice)
#         # if computer_choice == 1:
#         #     computer_choice = 'rock'
#         # elif computer_choice ==2:
#         #     computer_choice = 'paper'
#         # else:
#         #     computer_choice= 'scissors'

#         if player_choice==computer_choice:
#             print("choice your option")
#         elif player_choice=="rock" or computer_choice=="scissors":
#             win()
#         elif player_choice=="paper" or computer_choice=="scissors":
#             lose()
#         elif player_choice=="scissors" or computer_choice=="paper":
#             win()
#         elif player_choice=="scissors" or computer_choice=="rock":
#             lose()
#         elif player_choice=="paper" or computer_choice=="rock":
#             win()
#         again=input("do you want play again? (y or no").strip()
#         if again=="n":
#             break

#         if player_choice==0:
#             if pick_number==0:
#                 win_lose_label.config(text="Its A Tie! spin again...")
#             elif pick_number==1:
#                 win_lose_label.config(text="paper cover rock! you lose....")
#             elif pick_number==2:
#                 win_lose_label.config(text="rock cutes smashes scissors! you win")

#         #if user piks paper
#         if player_choice==1:
#             if pick_number==1:
#                win_lose_label.config(text= "Its A Tie! spin again...")
#             elif pick_number==0:
#                 win_lose_label.config(text ="paper cover rock! you win....")
#             elif pick_number==2:
#                 win_lose_label.config(text= "scissors cutes paper! you loss")

#         #if user piks scissors
#         if player_choice==2:
#             if pick_number==2:
#                 win_lose_label.config(text="Its A Tie! spin again...")
#             elif pick_number==0:
#                 win_lose_label.config(text = "rock smashes scissors! you lose....")
#             elif pick_number==1:
#                win_lose_label.config(text="scissors cutes paper! scissors! you win")


# #make our choice
# player_choice=ttk.Combobox(root,value=("rock","paper","scissoir"))
# player_choice.current(0)
# player_choice.pack(pady=20)

# #create a spin button
# spin_button=Button(root,text="spin!",command=spin)
# spin_button.pack(pady=10)

# exit_button=Button(root,text="exit!",command=exit)
# exit_button.pack(pady=100)

# #label for showing if you won or not
# win_lose_label=Label(root,text=var.get(),font=("Helvetica",18))
# win_lose_label.pack(pady=50)


# root.mainloop()
