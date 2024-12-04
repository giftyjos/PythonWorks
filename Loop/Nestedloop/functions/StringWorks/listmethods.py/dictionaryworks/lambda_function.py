# lambda functions for adding 2 numbers 

# def add_number(num1,num2):
#     return num1+num2
# print(add_number(100,200))#4300

add=lambda num1,num2:num1+num2

print(add(10,20))


# .....nxt qn...

# def cubenum():
#   return num**3

#   cube=lambda num:num**3
#   print(cube(num=num**3))


# ......qn.......

# lambda function for subtracting 2 numbers

sub=lambda n1,n2:n1-n2

print(sub(10,2))

# lambda function for finding cube of a number

cube=lambda n:n**3

# ....q....

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("hai","morning"))



# def smart_sub(num1,num2):

#     return num1-num2 if num1>num2 else num2-num1

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,100)) 

# .....qn.....

words=["hello","hai","morning","test"]

def get_length(word):
    return len(word)
print=(max(words,key=get_length))



words=["hello","hai","morning","test","apple"]
get_length=lambda word:len(word)
print(max(words,key=get_length))