#string "sequence of characters"

# string =>objects class

# class
# object




# capitalize() these are the methods
# casefold()
# isalpha()
# isdigit()
# isalnum()
# startswitch(str)
# endswith(str)
# split(",")
# replace(" ")


text="hellopython"
print(text.capitalize())


text="hellopython"
print(text.casefold())


text="hellopython"
print(text.isalpha())



text="hellopython12"
print(text.isdigit())


text="hellopython12"
print(text.isalnum())



text="hellopython"
print(text.startswith("he"))



text="hellopython"
print(text.endswith("on"))



text="hellopython"  #ch  one by one charcters print   ch -varrible  in-operator

#for ch in text:

    #print(ch)

# print vowels

text="hellopython"

text=text.casefold()#hellopython

for ch in text:

    if   ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":


         print(ch)
         




text="hello, world,python"

words=text.split(",")

print(words)



text="\t this is \ta line\t"

# remove \n

new_text=text.strip("\t")

# print(new_text)
# lstrip()
# rstrip()

text="hello world program"

# o => a

new_text=text.replace("o","a")

print(new_text)


text="python programming"
   
    # 0123456678901234567
    # string_object[start:end:step]

print(text[:6])

print(text[7:])

print(text[::2])

string="hello"


reversed_text=string[::-1]

print(reversed_text)



text=input("enter text")

reverse_string=text[::-1]

if text==reverse_string:

    print("palindrome")

else:

    print("not palindrome")

# print("palindrome" if text==reversed_string else "'not palindrome")



text="malayalam"
# index012345678
# len 123456789
length=len(text)-1 #9-1

reversed_str=""

for i in range(length,-1,-1):

    reversed_str+=text[i]

print(reversed_str)


text="hello world"
#     0123456789
#  index of first o
# text.replace()
# text.index("o") => 4

print(text.index('o'))


text="vipinkumar@gmail.com"

# find index of @
#  slice text from 0: index of slice

at_index=text.index("@")

username=text[0:at_index]
print(username)
  #or
print(text[0:text.index("@")])
# nxt qn
text="hellopython"

# llehopython

# sample2
# input="pythonprogramming"
# output="hythonprogramming"

# find index of o
# slice element upto o
# reverse 

#    012333345678910

o_index=text.index("o")

reverse_sub_str[o_index-1::-1]

balance_sub_str=text[o_index:]

result=reversed_sub_str+balance_sub_str

print(result)

# sample input 1
text1="PQRS"

text2="ABCD"

# q)merge two strings
#  output PAQBRCST


# sample input2


text1="PQRST"
text2="ABC"

# output:PAQBRCST

text1="PQR"
#      012

text2="ABC"
#      012

# output="PAQBRC"

result=""

for i in range(0,3):#i=0

    result+=text1[i]+text2[i]

print(result)










