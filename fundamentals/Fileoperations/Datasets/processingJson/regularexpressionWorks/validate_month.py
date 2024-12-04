from re import fullmatch

date=input("enter date")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,date)

if matcher==None:
    print("invalid")
else:
    print("valid")

    
# validate month 01-12
# dat 1 2 3 4 5 6 7 8
#     01 02 03 04 05 06 07 08 09
#     10 11 12