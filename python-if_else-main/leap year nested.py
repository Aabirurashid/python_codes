# year=int(input("enter the year"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")


# l = input("Input a letter of the alphabet: ")


# if l in ('a', 'e', 'i', 'o', 'u'):
# 	print("%s is a vowel." % l)
# elif l == 'y':
# 	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
# else:
# 	print("%s is a consonant." % l) 

# ch = input("Please Enter Your Own Character : ")

# if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
#     print("The Given Character ", ch, "is an Alphabet") 
# elif(ch >= '0' and ch <= '9'):
#     print("The Given Character ", ch, "is a Digit")
# else:
#     print("The Given Character ", ch, "is a Special Character")


# basic_salary = int(input("Enter your basic salary: "))

# if basic_salary > 25000:

#    hra = .35 * basic_salary

#    da = .95 * basic_salary

# elif basic_salary > 15000:

#    hra = .30 * basic_salary

#    da = .90 * basic_salary

# else:

#    hra = .25 * basic_salary

#    da = .80 * basic_salary

# gross_salary = basic_salary + hra + da

# print(f"The gross salary is {gross_salary}.")

# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])