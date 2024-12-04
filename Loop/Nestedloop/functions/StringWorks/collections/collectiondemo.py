

    # define is                                duplicate- allowed   insertion_order_preserved mutable methods

# list => []  this is list means square bracket    allowed                   yes                   yes

# or () this bracket

# tuple

numbers=[]


text="hello"
text2='hello'

text="""hellom there"""

text=str("hai")

str() #these are string


# list


expenses=[10000,12000,13000,11000]
#         0     1      2     3

print(expenses[1])

# 

colors=["red","green","blue"]

print(colors[1])

# empty list

colors=list()
print(type(colors))
# 

colors={"red","green","blue","green","blue"}

print(colors)  #duplicates not allowed not printed see in the ouput


colors=["red","green","blue","green","blue"]

colors[0]="pink"

print(colors) #red place pink varum


# example

expenses=[12000,13000,14000,11000,13000]
expenses[0]=15000
print(expenses)

# oro expenses separate print cheypikan

expenses=[12000,13000,14000,11000,13000]
# for exp in expenses:
#     print(exp)

    #  total_expenses

# total=0

# for exp in expenses:
#         total+=exp
# print(total)

#  max_expenses without using max()

max_exp=0

for exp in expenses:#exp=1000

    if exp> max_exp:#10000>13000

        max_exp=exp#max_exp=13000

    print(max_exp)


    # min
    # avg
    # most frequent exp 