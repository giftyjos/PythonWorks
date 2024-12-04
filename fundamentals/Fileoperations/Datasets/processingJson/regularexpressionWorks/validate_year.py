from re import fullmatch

pattern="((18|19)[0-9]{2}|20[01][0-9|202[0-4])"


year=input("enter year")

matcher=fullmatch(pattern,year)


print("invalid" if matcher==None else "valid")


# validate gmailid

# lowercase
# start with an alphabet
# numbers optional
# @gmail.compile
# before at 64 charcters