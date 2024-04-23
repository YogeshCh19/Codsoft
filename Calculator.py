print("*****************CALCULATOR********************")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("select an option to perform operation in between the operands ")
print("1. ADDITION (+)")
print("2. SUBTRACTION (-)")
print("3. MULTIPLICATION (*)")
print("4. DIVISION (/)")
print("5. EXPONENTIAL POWER (**)")
n=int(input())
if n==1:
    print("Addition of your first and second number is:",a+b)
elif n==2:
    print("Subtraction of your first and second number is:",a-b)
elif n==3:
    print("Multiplication of your first and second number is:",a*b)
elif n==4:
    print("Division of your first and second number is:",a/b)
elif n==5:
    print("Exponentioal Power of your first and second number is:",a**b)
else:
    print("enter valid option")