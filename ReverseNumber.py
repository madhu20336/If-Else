number=int(input("enter the number: "))
first_number=number%10
second_number=(number//10)%10
third_number=(number//100)%10
new_number=(first_number*100)+(second_number*10)+(third_number*1)
if number<=1000:
    print(new_number)
else:
    print("it can't reverse number")