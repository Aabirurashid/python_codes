# import json
# print("**WELCOME THE LOGIN AND SIGNUP PAGE**")
# user=input("what do u want login or signup:")
# if user=="signup":
#     user_name=input("enter the user name:")
#     password1=input("enter the password:")
#     password2=input("confirm the password:")
#     if password1==password2:
#         if password2 in "A-Z" or "a-z"and password2 in "2" or "8" and password2 in "$"or"2":
#             print("ur pasdsword is strong")
#             description=input("enter the discription:")
#             dob=input("enter the DOB :")
#             hobbies=input("enter the Hobbies:")
#             gender=input("enter the gender M/F:")
#             print("congrts",user_name,"u yave suessfully signuped")
#             user_details={"user_name":user_name,"password2":password2,"description":description,"DOB":dob,"hobbies":hobbies,"gender":gender}
#             with open("user.json","a")as file:
#                 a=json.dump(user_details,file,indent=4)
#                 # print(a)
#         else:
#             print("ur password is not strong")
#     else:
#         print("ur password is wrong")

# elif user=="login":
#     name=input("enter the user_name:")
#     password=input("enter the password:")
#     with open("user.json","r") as file:
#         data=json.load(file)
#         if password==data["password2"]:
#             print("ur account has been logged sucessfully")
#             print("ur information is correct")
#             print(data)

# else:
#     print("ur information is wrong:")
# a=[5,8,7,9,22,66,99,120]
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
# print("before:",a)
# i=1
# c=[]
# while i<=len(a):
#     c.append(a[-i])
#     i=i+1
# print("now:",c)



from bs4 import BeautifulSoup
import requests
import json

movie_details=[]
def scrap_movie_details(link):
    d1={}
    link_data=requests.get(link)
    # print(link_data)
    soup=BeautifulSoup(link_data.text,'html.parser')
    # print(soup)
    d1["name"]="Black panther"
    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    # print(movie_bio)
    d1["Bio"]=movie_bio
    title=soup.find_all("div",class_="meta-label subtle")
    # print(title)
    value=soup.find_all("div",class_="meta-value")
    # print(value)

    for i in range(len(title)):
        d1[str(title[i].get_text().strip())[:-1]]=value[i].get_text().strip()
    movie_details.append(d1)
    with open("scrap_movie.json","w")as file:
        json.dump(movie_details,file,indent=4)

        

scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")