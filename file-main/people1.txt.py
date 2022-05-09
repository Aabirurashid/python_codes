# my_file = open("people1.txt","r")

# file_data = my_file.read()

# print (file_data)

# my_file.close()

# my_file2 = open("people2.txt", "w")

# my_file2.write("Abhishek - Gurgaon\n")

# my_file2.write("Ranveer - Delhi")

# my_file2.close()

# print ("AbhishekRanveer")

# print ("---------------------------------")

# print ("Abhishek\nRanveer")

# print ("---------------------------------")

# print ("Abhishek\n\nRanveer")

# print ("---------------------------------")

# my_file3 = open("people3.txt", "w")

# my_file3.write("Abhishek - Gurgaon\n")

# my_file3.write("Ranveer - Delhi")

# my_file3.close()

# batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]

# students_file = open("navgurukul_students.html", "w")

# students_file.write("<html>\n")

# students_file.write("<head>\n")

# students_file.write("<title>NavGurukul Students</title>\n")

# students_file.write("</head>\n")

# students_file.write("<body>\n")

# students_file.write("<ul>")

# for student in batch1_students:

#     students_file.write("<li>" + student + "</li>\n")

# students_file.write("</ul>\n")

# students_file.write("</body>\n")

# students_file.write("</html>\n")

# students_file.close()


# my_file3 = open("test_file.txt", "w")
my_file = open("people1.txt","r")

# file_data = my_file.read()

# print (file_data)

# my_file.close()
# my_file3.write("Yahan main kuch likha")

# my_file3.write("\nYaha maine kuch aur bhi likha.")

# my_file3.close()

# my_file3.write("Kuch aur likhte hain")


obj=open("student.txt","w")
name=[]
for i in range(5):
    value=input("enter name")
    name.append(value+"\n")
obj.writeline(name)
obj.close()
