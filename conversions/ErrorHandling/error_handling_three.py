num1=int(input("enter num1"))#10

num2=int(input("enetr num2"))#0

try:
    result=num1/num2 #10/0
    print(result)
except:
    num2=int(input("enter number2"))
    result=num1/num2
    print(result)
finally:

  print("file operation")
  print("database commit")