
# rule 10 digit
# validate mobile number

from re import fullmatch

mobile_number=input("enter mobile number :")

pattern="(91)?[0-9]{10}" #[0-9]* means ethranumber venamenkilum varamn aan soo...nam {10} kodth

# quantifier ? means varam varathirikam(optional)
# * asteric means anynumber
# + oru thavanekilum varam

matcher=fullmatch(pattern,mobile_number)

if matcher==None:
     
     print("invalid")
else:
    print("valid")
