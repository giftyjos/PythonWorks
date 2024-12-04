
# smart_sub(n1,n2) 
def round_decorator(fn):
    def wrapper(num1,num2):
        num1=round(num1)
        num2=round(num2)


        return fn(num1,num2)
    return wrapper

@round_decorator
@swap_decorator
def add_number(num1,num2):
    
    return num1+num2#10+2

@round_decorator
@swap_decorator
def subtraction(num1,num2):

    return num1-num2

@round_decorator
@swap_decorator

def division(num1,num2):
    return num1/num2

print(division(2,10))

print(add_number(2,5,3,6))

print(subtraction(2,8,12,2))

# # DRY(donot reapet you)
# print(smart_sub(10,2))#10-2=8
# print(smart_sub(2,10))#2-10=-8

# print(smart_div(10,2))
# print(smart_div(2,10))