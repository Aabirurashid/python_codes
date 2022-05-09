tax=0
price=int(input("enter the price of bike"))
if price> 100000:
    tax=15/100*price

elif price>50000 and price<=100000:
    tax=10/100*price

else:
    tax=5/100*price

    print( "tax to be paid")