# add(obj)
colors={"red","green","blue"}
colors.add("yellow")
print(colors) #add(obj) method


# intersection()
st1={10,20,30,40,50}
st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)
print(intersection_set)


# union()
# print(intersection_set)
# 10,20,30,40,50,60,70,80 union()

Union_set=st1.union(st2)

print(Union_set)

# difference()

difference_set=st1.difference(st2)
print(difference_set)

# remove()

st1={10,20,30,40,50}
st1.remove(50)
print(st1)