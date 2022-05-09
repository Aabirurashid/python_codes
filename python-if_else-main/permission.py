day=input("decide the day:")
if day=="sunday":
    print("u can go")
    permission=input("enter the name of person whom you take the permission:")
    if permission=="disco": 
        print("ok!you can go but before you also take the permission from rose dii")
        permit=input("enter the name from whom you take the permission:")
        if permit=="Rose dii":
            print("you can go but carefully and take care!")
            place=input("enter the place for where you are going:")
            if place=="hospital":
                print("ok but only for hospital only")
                time=int(input("enter the time,when you come back the campus:"))
                if time==7:
                    print("ok")
                    quarantine=int(input("enter the days of quarantine :"))
                    if quarantine ==14:
                        print("ok!after 14 days you can come outside:")
                    else:
                        print("no u can not come outside after 14days")
                else:
                    print("not ok")
            else:
                print("you can go anywhere")
        else:
            print("you can not go anywhere")
    else:
        print("don,t take the permission")
else:
    print("no u can not go")