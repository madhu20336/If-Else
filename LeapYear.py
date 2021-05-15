Year=int(input("enter a year: "))
if Year % 4 == 0 :
    if Year % 100 != 0 or Year % 400 == 0:
        print(Year,"is leap year ")
else:
    print(Year,"is normal year")