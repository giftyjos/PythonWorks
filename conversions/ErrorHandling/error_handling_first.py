num1=int(input("enter num1"))#10

num2=int(input("enter num2"))#0

try:
    result=num1/num2 #10/0 error
    print(result)#5.0

except Exception as e :
    print(e)#error

print("file write")#fw
print("database commit")#dc                                  (try:doubtfullcode ,except:handling means error handling)