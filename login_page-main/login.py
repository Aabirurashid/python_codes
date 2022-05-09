import json
print("**WELCOME THE LOGIN AND SIGNUP PAGE**")
user=input("what do u want login or signup:")
if user=="signup":
    user_name=input("enter the user name:")
    password1=input("enter the password:")
    password2=input("confirm the password:")
    if password1==password2:
        if password2 in "A-Z" or "a-z"and password2 in "2" or "8" and password2 in "$"or"2":
            print("ur pasdsword is strong")
            description=input("enter the discription:")
            dob=input("enter the DOB :")
            hobbies=input("enter the Hobbies:")
            gender=input("enter the gender M/F:")
            print("congrts",user_name,"u yave suessfully signuped")
            user_details={"user_name":user_name,"password2":password2,"description":description,"DOB":dob,"hobbies":hobbies,"gender":gender}
            with open("user.json","a")as file:
                a=json.dump(user_details,file,indent=4)
                print(a)
        else:
            print("ur password is not strong")
    else:
        print("ur password is wrong")

elif user=="login":
    name=input("enter the user_name:")
    password=input("enter the password:")
    with open("user.json","r") as file:
        data=json.load(file)
        if password==data["password2"]:
            print("ur account has been logged sucessfully")
            print("ur information is correct")
            print(data)

else:
    print("ur information is wrong:")

