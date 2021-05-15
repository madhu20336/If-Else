quantity=int(input("enter quantity: "))
if quantity*100>1000:
    print("cost is",quantity*100)-(quantity*100//10)
else:
    print("cost is ",quantity*100)