# read two numbers print largest number


#print=("enter two number:")

#if num1>num2:

    #print(f"{num1} largest number")

#else:
    #print(f"{num2} largest number")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} greater than {num2} ") 
elif num2>num1:
    print(f"{num2} greater than {num1}")

else:
    print("all are equal")
