age1=int(input("enter the age: "))
age2=int(input("enter the age: "))
age3=int(input("enter the age: "))
if age1 > age2 and age1 > age3:
    print("oldest age is ",age1)
elif age2 > age3 and age2 > age1:
    print("oldest age is",age2)
elif age3 > age1 and age3 > age2:
    print("oldest age is",age3)
else:
    print(age1,age2,age3,"equale age") 