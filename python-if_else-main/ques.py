app=input("enter your app")
if app=="whatsup":
    print("open your whatsup")
    internet=input("check is he or she online or offline")
    if internet=="on":
        print("she is online")
        first_chat=input("enter your message")
        if first_chat=="Assalam aliakum":
            print("walaikum assalam")
            second_chat=input("enter the next message")
            if second_chat=="how are you":
                print("i am fine and what about you")
                print("i am also fine")
                third_chat=input("enter the next message")
                if third_chat=="are you ate lunch":
                    print("yes i am eaten lunch at 2,o,clock")
                    fourth_chat=input("enter next message")
                    if fourth_chat=="ok bye take care":
                        print("bye same to u")
                    else:
                        print("hii")
                else:
                    print("i am not ate lunch till")
            else:
                print("not fine")
        else:
            print("sorry i can,t reply you")
    else:
        print("she is offline")
else:
    print("facebook")