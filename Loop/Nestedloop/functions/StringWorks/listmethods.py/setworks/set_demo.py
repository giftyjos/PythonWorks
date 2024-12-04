
# set

# lst=[]
# tp=()

st=set() #set

# print(type(st))

set={"red","green","blue"} #this is set values ind athond then..another way set={} not a set this is a dictionary

print(set)


st={10,20,30,10,20,30,"hello","hai"}# insertion order support cheyila

print(st)   #set il index support cheyila set doesnot support indexing


colors={"red","green","blue"}
colors.add("yellow")
print(colors) #add(obj) method


colors=["red","green","red","blue"]
colors_set=set(colors)
print(colors_set)



st1={1,2,3}
st2={1,2,3,4,5}

print(st1.issubset(st2))#true


print(st2.issuperset(st1))


st1={1,2,3,10,20}
st2={1,2,3,4,5}

# 10,20,4,5

symmetric_difference=st1.symmetric_difference(st2)
print(symmetric_difference)#(AUB)-(A^B)

st1.update(st2)
print(st1)

text="this is a test remove duplicate words this is simple"
# split text wrt space
text2="this simple test remove duplicate words"
words=text.split(" ")

print(set(words))