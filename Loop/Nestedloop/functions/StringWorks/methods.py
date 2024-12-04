# class list:  these are the ,methods

     # def append(self):

      # def pop()
       
    # def index() ("object indenkil" alenkil  error kaanikum)

    # def copy()

    # def insert()


colors=["red","green","blue"]
        #  0    1      2 index

# colors.append()#insert new object end of the list

# colors.append("yellow")

# print(colors)


# colors.pop()remove the last object from list and return it

# popped_element=colors.pop()

# print(colors)

# colors.pop(1)

# print(colors)



red_index=colors.index("red")#return index of first occurance red
print(red_index)


# copy

praveen_fvt_colors=["blue","yellow","blck","white"]

abishek_favt_colors=praveen_fvt_colors.copy()

abishek_favt_colors.pop()


print("abi favt",abishek_favt_colors)

print("prv fvt",praveen_fvt_colors)




list=[2,6,3,4,5,6]

# list.sort()

list.sort(reverse=True)

print(list)



frutis=["apple","orange","mango"]

products=["onion","potato","brinjal"]

products.extend(frutis)

print(products)