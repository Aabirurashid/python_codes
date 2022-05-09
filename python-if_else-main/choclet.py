time= float(input("enter the time"))
if (time >= 6.30 )and (time <= 7.30):
  print("morning exercise")
elif (time>= 7.30) and (time <= 8.30):
  print("break")
elif (time >=8.30 ) and (time<= 9.00):
  print("break fast")
elif (time<=9.00) and (time<=10.00):
 print("english activity")
elif time>=11.00 and 13.00:
 print("coding")
elif time>=13.00 and time<14.30:
 print("lunch break")
elif time >=14.30 and time <=17.30:
 print("again coding")
elif time>=17.30 and time <= 18.30:
    print("culture activity")
elif time >= 18.30 and time <= 19.30:
 print("break")
elif time >=19.30 and time <= 22.30:
    print("again coding")
elif time >= 22.30 and time <= 24.00:
 print("dinner")
else:
 print("lights off")
