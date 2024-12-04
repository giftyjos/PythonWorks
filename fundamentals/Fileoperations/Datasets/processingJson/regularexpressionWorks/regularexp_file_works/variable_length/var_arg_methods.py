# def add_numbers(*args): #accept any number of aruguments as tuple

#     print(args)

# add_numbers(10,20)
# add_numbers(10,20,30)

# def product(*args):
#     result=1

#     for num in args:
#         result=result*num
#     return result
# # print(product(10,20))
# print(product(10,20,5,6))



def add_numbers(*args):
    return sum(args)
print(add_numbers(10,20))
print(add_numbers(10,20,30))
print(add_numbers(10,20,40,50))


# create a function that accept any number of argument and return second maximum number

def second_max_number(*args):
    sorted_numbers=sorted(args,reverse=True)#[13,12,11,10]
    return sorted_numbers[1]

print(second_max_number(10,11,12,13))
print(second_max_number(10,11,12,13,14,15))




# this is an asteric (*) progrm how to use means tuple can use  (tuple aayit avrum (*) oru asteric)

# ....nxt.......

def display_mobile_data(**kwargs): #means keyword argument

    print(kwargs.get("name"))

    print(kwargs.get("price"))

display_mobile_data(name="oneplus",price=32000,display="amoled")

# (**)two asteric can use keyword argument(kwargs) is  dictonary 






# ......nxt....

def calculator(*args,**kwargs):

    # args=(10,20,30)
    # kwargs={"operation":"+"}

    if kwargs.get("operation")=="+":
        return sum(args)
    if kwargs.get("operation")=="*":
        result=1
        for num in args:
            result=result*num
        return result 
print(calculator(10,20,30,operation="*"))

# ......nxt qn.....

# def student_info(45,43,44,operation="avg")
# def student_info(45,43,44,operation="total")


def student_info(*args,**kwargs):
    if  kwargs.get("operation")=="total":
        return sum(args)
    if kwargs.get("operation")=="avg":
        return sum(args)/len(args)

print(student_info(45,43,44,operation="total"))# student_info(45,43,44,operation="total")

# .....nxt.....
# def sort_number(1,2,6,4,11,15reverse="True")descending order
# def sort_number(1,2,6,4,11,15reverse="False")ascending order

def sorted_numbers(*args,**kwargs):

    if kwargs.get("reverse")=="True":
        return sorted(args,reverse=True)
    if kwargs.get("reverse")=="False":
        return sorted(args)
print(sorted_numbers(1,2,6,4,11,15,reverse="True"))





