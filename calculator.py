#Simple Calculator using Arthimetic Operators

def cal(a,b):
    operator=input("Enter the operator to perform operation:")

    if operator == '+':
        c=a+b
        print( a,"+",b,"=",c)

    elif operator == '-':
        c=a-b
        print(a,"-",b,"=",c)

    elif operator == "*":
        c=a*b
        print(a,"*",b,"=",c)

    elif operator == "/":
        c=a/b
        print(a,"/",b,"=",c)

    elif operator == "**":
        c=a**b
        print(a,"**",b,"=",c)

    elif operator == "%":
        c=a%b
        print(a,"%",b,"=",c)

    else:
        print("Invalid Choice")
        
        
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
cal(a,b)

while(True):
    repeat=input("enter y/n to proceed:")

    if repeat.lower()=="y":
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        cal(a,b)
    else:
        break
       
    

    




