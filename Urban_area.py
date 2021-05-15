age=int(input("enter the age: "))
sex=input("enter the sex: ")
marry=input("enter the condition: ")
if sex == "Female":
    print("She will work only in urban areas")
elif sex == "Male" and age >= 20 and age <=40:
    print("He  may work in any where ")
elif sex == "Male" and age >=40 and age <= 60:
    print("He will work in urban areas only")
else:
    print("error")