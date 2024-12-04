# factorial of 5   1*2*3*4*5

number=int(input("enter value :"))#5
fact=1
for num in range(1,number+1):
    fact=fact*num
print(fact)