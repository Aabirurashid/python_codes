name=input("enter the atm name:")
if name =="Indian atm bank":
    print("welcome to Atm bank")
    card=input("enter the  card")
    if card=="card insert" or "debit cart":
        print("yes")
        lunguage=input("enter the lunguage")
        if lunguage=="english" or "hindi" or "urdhu":
            print("yes")
            pincode=input("enter the pincode")
            if pincode=="1213":
                print("yes")
                account=input("enter type of account")
                if account=="saving" or "current":
                    print("yes")
                    withdrawal=input("enter the withdrawal")
                    if withdrawal=="saving":
                        print("yes")
                        amount=int(input("enter the amount"))
                        if amount<=10000:
                            print("amount preped")
                            recipt=input("i want recipt")
                            if recipt=="yes":
                                print("no thanks")
                            else:
                                print("thanks")
                        else:
                            print("no") 
                    else:
                        print(" amount not preped")
                else:
                    print("no") 
            else:
                print("wrong pincode")   
        else:
            print("no")   
    else:
        print(" try again")
else:
    print("0ther atm bank")
