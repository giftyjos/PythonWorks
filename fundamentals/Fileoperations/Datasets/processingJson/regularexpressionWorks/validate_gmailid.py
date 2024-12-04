from re import fullmatch

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

date=input("enter gmail")

matcher=fullmatch(pattern,gmail_id)

print("invalid" if matcher==None else "valid")





# validate gmailid

# lowercase
# start with an alphabet
# numbers optional
# @gmail.compile
# before at 64 charcters