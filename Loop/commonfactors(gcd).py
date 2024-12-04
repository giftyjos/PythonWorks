

num1=int(input("enter number1:"))#16

num2=int(input("enter number2:"))#24

# for i in range(1,num1+1):

#     if num1%i==0 and num2%i==0:

#         print(i)

# gcd of (15,30)

gcd=1

min_num=min(num1,num2)

for i in range(1,min_num+1):#(for loop works 1,,,,16)

    if num1%1==0 and num2%i==0:

      gcd=i#(i means 16 24 common factor latest value 16 printed)

print(gcd)#(i assign last value printed)





