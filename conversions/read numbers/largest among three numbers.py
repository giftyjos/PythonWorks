#read three numbers num1,num2,num3 print  largest number amoung three numbers

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))

# if num1 > num2 and num1 > num3:
#  print("largest number is {num1}")
# elif num2 > num1 and num2 > num3:
#  print({num2} "is the largest number")
# elif num3>num1 and num3>num2:
# print({num3} "is the largest number")
# else:
#     print("all are equal")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    
    print(f"largest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest number")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is the largest number")
else:
    print("all are equal")

