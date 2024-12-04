#           i
# i  0 1 2 3 
arr=[2,3,4,5,7,8]
#    0 1 2 3
#            j 
sum=int(input("enter sum")) #or  8,sum=7

# (2,5)(3,4)(5,3)
count=0

for i in range(0,len(arr)-1):

    for j in range(i+1,len(arr)):

        count+=1

        cur_sum=arr[i]+arr[j] #cur_sum=current sum

        if sum==cur_sum:

            print(arr[i],arr[j])

            break
print(count)

        # list=[2,3,4,5]

        # 12,11,10,9

        # sample input2

        # list=[3,6,7]
        # 13,10,9




        # T1
        # App1(20mint)
        # App2(5mint)
# arr=[2,3,4,5,7,8,9]
# #    0 1 2 3 4 5 6
# #    1          r
# left=0
# right=len(arr)-1
# while(left<right):

#  cur_sum=arr[left]+arr[right]

# #  cur_sum==sum=>print pairs
# #  cur_sum>sum=>right=right-1
# #  cur_sum<sum left=left+1

#  if cur_sum==sum:
#     print(arr[left],arr[right])
#     break
#  elif cur_sum>sum:
#     right=right-1
#  elif cur_sum<sum:
#     left=left+1
