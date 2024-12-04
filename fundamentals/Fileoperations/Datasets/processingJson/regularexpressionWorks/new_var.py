# starting with an alphabets from p-t
# in second place mustbe a  number that is \ by 3
# followed by anynumber alphabets,numbers,@

# s6abc
# a6vvhvh
# s7bc

from re import fullmatch

pattern="[p-tp-T][369][a-zA-z0-9@]*"

user_input=input("enter variable name")

matcher=fullmatch(pattern,user_input)

if matcher==None==None:
     
     print("invalid")
else:
    print("valid")
