
# create a function that take two parameter num1,num2

def sum(num1,num2):
    result=num1+num2
    print(result)

sum(100,200)


# cube print

def cube(num):

    result=num**3
    print(result)
cube(3)



#q1 sub(num1,num2)
#q2 multiplication(num1,num2)
#q3 division(num1,num2)  -hw


def print_course_details(course_name="",company_name=""):
    print(course_name)
    print(company_name)
print_course_details("LUMINAR","django")



# create a function last_digit_max with two parameter num1,num2
# num1=123
# num2=872
# num1

def last_digit_max(num1,num2):
    num1_last_digit=num1%10
    num2_last_digit=num2%10
    print(num1 if num1_last_digit>num2_last_digit else num2)
print(last_digit_max(123,871))



# create a function is_prime(num)
# create function factorial(num)  -hw








def factorial(num):
    fact=1
    for i in range (1,num+1):
        fact=fact*i

    return fact

result=factorial(3)
print(result)



#create a function num_chck retrun odd if number is odd else return even
                                                
                                                   #def is_odd(number): 
def num_chk(number):                               #if number%2==0:
                                                        #return False
                                                    # else:
                                                        # return True
                                                        # is_odd(10)
     return"even" if number%2==0 else "odd"    
print(num_chk(10)) 



# create funtion max_two with two parameter num1,num2 return largest number


def max_two(num1,num2):

    return num1 if num1>num2 else num2

print(max_two(100,200))

# create funtion min_two with two parameter num1,num2 return smallest number

def min_two(num1,num2):

    return num1 if num1<num2 else num2

print(min_two(100,200))


# block colon: used
# if:
# else:
# elif:
# for:
# while:
# def:
# class:
# try:
# except:
# finally:


""" create a function multiplication_table(number,n)
print multipilcation table of number till n"""

# multiplication_table(3,50)

def multiplication_table(number,n):#3,5
  for i in range(1,n+1):

    print(f"{i}*{number}={i*number}")

multiplication_table(3,10)



# create a fuction exponet with two parameter num1,n


def expo(number,n=2):
    return number**n
print(expo(6))


# create a function smart_sub with three parameter num1,num2,reverse
# reverse takes boolean value
# if reverse==True then return num2-num1 else return num1-num2


def smart_sub(num1,num2,reverse):

    # smart_sub(2,10,True)#10-2

    # smart_sub(2,10,False)# 2-10
 
      return num2-num1 if reverse==True else num1-num2

print(smart_sub(10,20,True))


# create a function random_numbers(start,end,step)

# print numbers from start to end

# random_numbers(1,7,2)#1,3,5



# start=int(input("enter number"))

# end=int(input("enter number"))

# def random_numbers(start,end,stop):

#     i=start

#     while(i<=end):

#         print(i)


def random_numbers(start,end,step=1):
 
    while(start<=end):

        print(start)

        start=start+step

random_numbers(10,100,2)

# create function

# def function_name(arg1,arg2,arg3,,,,,,arg=defaultvalue):
# function definition
# return
# function_name(p1,p2)


#is_perfect_number(number)
# is_armstrong_number(number)
# is_palindrome_number(number) 

# HW






 





    