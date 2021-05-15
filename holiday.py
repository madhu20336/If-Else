day=input("enter the day: ")
if day == "thursday":
    print("holiday")
    place=input("enter the place: ")
    if place == "hospital":
        print("Go to hospital")
        permision=input("enter the permision: ")
        if permision == "yes":
            print("Go to out side ")
            precosion=input("enter the precosion: ")
            if precosion == "sentizer,mask":
                print("take proper precosion")
                Type=input("enter the type: ")
                if Type == "persional work":
                    print("you are quarantine in 7 days")
                else:
                    print("you are not quarantine")
            else:
                print("make social distance")
        else:
            print("Sorry you are not go outside")
    else:
        print("you are not go to outside")
else:
    print("That day  is not holiday")