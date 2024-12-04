# sample input


# arr=[100,800,300,600,500,00,700,800]
#    0    1   2   3   4  5   6    7
#                 L       R
# output

# odd_position_element[200,400,600,800]

# reverse=[800,600,400,200]
# insert these elements into odd_position

# result=[100,800,300,600,500,400,700,200]

# sample input2

# arr=[10,20,30,40,50,60]
#    0  1   2  3  4  5

# result=[10,60,30,40,50,20]



odd_position_elements=[arr[i] for i in range(0,len(arr)) if i%2!=0]

print(odd_position_elements)

for i in range(1,len(arr),2):
     element=odd_position_elements.pop()
     arr[i]=element
     print


