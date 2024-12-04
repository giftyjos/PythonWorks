



box=[
    {"color":"green","size":2},
    {"color":"green","size":7},
    {"color":"green","size":1},
    {"color":"green","size":5},
    {"color":"green","size":3},
    {"color":"green","size":8},

]





# count
# print(len(box))


# for b in box:#b={"color":"green","size:2"}
#     print(b.get("size"))
# for b in box:
#     print(b.get("color"))

# print(len(box))
# colors=[b.get("color") for b in box]
# print(colors)

# list comprehension

sizes=[b.get("size") for b in box]

print(sizes)