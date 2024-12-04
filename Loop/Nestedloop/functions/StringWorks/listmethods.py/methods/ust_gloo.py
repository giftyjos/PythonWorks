arr=[100,200,300,400,500,600,700,800]
#    0    1  2    3    4   5   6  7
# i
# enumarate(iterable)=> enumarate function use index object or number return it

# for num in arr:

#     print(num)

# for i in range(0,len(arr)):

#     print(i)

# for index,number in enumerate(arr):
    # print(index,number)


odd_position_number=[num for index,num in enumerate(arr)if index%2!=0]
odd_position_number.reverse()
print(odd_position_number)
i=1
for index,num in enumerate(odd_position_number):#index=0 number=800
    
    arr[i]=num
    i+=2
print(arr)

