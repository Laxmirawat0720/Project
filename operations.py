a=float(input("Enter any number= "))
b=float(input("Enter any number= "))

print("Select any operation given below:")
print("1.Addition\n" "2.Subtraction\n" "3.Multiplication\n" "4.Division\n")
operation=input("Select any number (1,2,3,4): ")

if operation=="1":
    result=a+b
    print("The addition between given two numbers are: ",result)

elif operation=="2":
    result=a-b
    print("The subtraction between given two numbers are: ",result)

elif operation=="3":
    result=a*b
    print("The Multiplication between given two numbers are: ",result)

elif operation=="4":
    if b==0:
        print("Division cannot be performed having denominator zero\n")
    else:
        result=a/b
        print("The division between given numbers are: ",result)

else:
    print("Invalid opration selected.Please select from(1,2,3,4).")