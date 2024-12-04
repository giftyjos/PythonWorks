from re import fullmatch

user_input=input("enter variable name ") #num_

# startwith an alphabet (lowercase,upercase)
# any number of alphabetd,digits,_

pattern="[a-zA-Z][a-zA-z0-9_]*"

matcher=fullmatch(pattern,user_input) #None

if matcher==None:
    
    print("invalid")

else:

    print("valid")

