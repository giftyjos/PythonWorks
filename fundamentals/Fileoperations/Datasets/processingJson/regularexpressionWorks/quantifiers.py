from re import finditer # this is an template

text="abbbababbabaaaab"
#     0123456789012345

# pattern="a{2}"

# pattern="a{1,3}" # min 1 max 3

pattern="a*" #* any number including 0 

# "[a-z]"-any no.of alphabets
# 
# a-z{2} [0-9]{2} [a-z]{1,2}[0-9]{4}*
#kl08ca4567

matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())