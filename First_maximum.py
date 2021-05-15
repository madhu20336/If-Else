num1=int(input("enter the number: "))
num2=int(input("enter the number: "))
num3=int(input("enter the number: "))
if num1 > num2 and num1 > num3:
    print("maximum number is", num1)
elif num2 > num1 and num2 > num3:
    print("maximum number is",num2)
elif num3 > num1 and num3 > num2:
    print("maximum number is",num3)
else:
    print("all number is equal")