num=int(input("Number of Girls: "))
if num==12:
    print("occupied")
elif num<12:
    print(12-num," bed are left")
else:
    print(num-12,"Girls shift in other room")