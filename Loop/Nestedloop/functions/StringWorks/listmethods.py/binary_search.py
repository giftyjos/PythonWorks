

# # [arr=[2,4,6,3,8,7]

# # 0 1 2  3 4 5
# #  i


# search_element=int(input("enter number"))

# is_present=False

# for i in range(0,len(arr)):

#     if search_element==arr[i]:

#         is_present=True

#         break
    
#     print(is_present)

#     ]


# binary search

arr=[10,8,7,12,20,25]

#read search element

search_element=int(input("enter number"))


arr.sort()

# step2 set low,upp

low=0

upp=len(arr)-1

is_present=False

while(low<=upp):


# find mid

 mid=(low+upp)//2

# case1
if search_element==arr[mid]:

    is_present=True

    break

elif search_element<arr[mid]:

    upp=mid-1

elif search_element>arr[mid]:
    low=mid+1
print(is_present)



