num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
symbole=input("enter a symbole: ")
if symbole=='+':
    print(num1+num2)
elif symbole=='-':
    print(num1-num2)
elif symbole=='*':
    print(num1*num2)
elif symbole=='%':
    print(num1%num2)
elif symbole=='/':
    print(num1/num2)
else:
    print("no any value")