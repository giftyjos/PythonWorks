# read three numbers num1,num2,num3 print second largest number  amoung three numbers

num1=int(input("enter  num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

if num1>num2 and num1<num3:
  print(f"{num1}is the second largest number")

elif num2>num1 and num2<num3:
    print(f"{num2} is the second largest number")
elif num3>num1 and num3<num2:
    print(f"{num3}is the second largest  number")

else:
    print("all are eqaual")
