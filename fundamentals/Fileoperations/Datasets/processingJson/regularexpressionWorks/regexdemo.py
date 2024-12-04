

from re import finditer

text="abababbaab"
#     0123456789
# ba
pattern="ab"

# finditer(pattern,text)#[object(start,grup),object(start,grup),object(start,grup)]


matcher=finditer(pattern,text) #[(start,group)]

for obj in matcher:
 
    print(obj.start(),obj.group())



# ...nxt qn...

from re import finditer

text="fatcatrunsveryfasttocaththerat"
#     012345678901234567890123456789
matcher=finditer("at",text)#[(start,grup),(),(),]

for obj in matcher:

    print(obj.groups())

    print(obj.start(),obj.group())