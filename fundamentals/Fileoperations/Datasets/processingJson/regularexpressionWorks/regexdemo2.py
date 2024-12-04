from re import finditer

text="I have 3 cars,2 bike and 1 cycle"
#     01234567890123456789012345678901

# pattern="[a-z]" # neither a or b #chck  all lowercase alphabets
# pattern="[a-zA-Z] #chk for all alphabets (lower and uppercase)
# pattern="[0-9]" #chck for all digit


# alphanumeric

# pattern="[a-zA-Z0-9]" #chck for all alphanumerics
# pattern="[^ak]" # ^,means exclude a,k this is anothrr meaning a-k a to k full povum

# all lower case alphabets exclde a,k

# pattern="[^akA-Z0-9,\-]" #\- hyphen excluding\
pattern="[^a-zA-Z0-9]" #chck for all special charcters-space coomma hyphen

matcher=finditer(pattern,text) #[(start=4,group=a),(start=11,group=a),(start=17,group=b),]

for obj in matcher:

     print(obj.start(),"==>",obj.group())


# pattern="[a-z]" #lowercase alphabets
# pattern="[A-Z]" #uppercase alphabets
# pattern="[a-zA-z]" #alphabets
# pattern="[0-9]" #digits
# pattern="[a-zA-Z0-9]" #alphanumeric
# pattern="[^a-zA-Z0-9]" #spcl charcters exclude

# predefined charcters
# quantifiers

