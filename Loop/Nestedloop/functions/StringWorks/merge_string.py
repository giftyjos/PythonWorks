text1="PQRST"
#      0123
     
text2="ABC"
#      012

smallest_text=text1 if text1<text2 else text2


largest_text=text1 if text1>text2 else text2

result=""

for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]



balance_text=largest_text[len(smallest_text):]

result+=balance_text
print(result)



# data types
# int,float,str
# sequence=> str
# boolean>bool


# collection type
# list
# tuple
# set
# dictionary



# shirts store(500 shirts)

# size organise L M XL color price

# medicine 500medicine (1m xl white brand)  A=>a b=>b