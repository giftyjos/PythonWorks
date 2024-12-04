arr1=[10,13,8,11,20]
     # 0  1 2  3  4  
arr2=[2,20,8,7,13]


# common elements without using "in" 13,20,8

for i in range(0,len(arr1)):

 for j in range(0,len(arr2)):

  if arr1[i]==arr2[j]:

    print(arr1[i])


  # sample qn 1
    arr1=[1,2,3,4,5]
    # find missing +ve integer 2

  # sample qn2

    arr2=[1,2,3,5]  #6
# 
  arr1.sort()

  arr2.sort()

  p1=0

  p2=0

  while (p1<len(arr1) and p2<len(arr2)):

      if arr1[p1] == arr2[p2]:

        print(arr1[p1])

        p1+=1
        
        p2+=1


      elif  arr1[p1]<arr2[p2]:

          p1+=1

      elif arr1[p1] > arr2[p2]:

        p2+=1

 # sample qn 1
  arr1=[1,2,3,4,5]
    # find missing +ve integer 2

  # sample qn2

  arr2=[1,2,3,5]  #6


  arr.sort()
  
  #  
  # arr.sort

  #  duplicate_number

  #   for i in range(0,len(arr)-1):

  #     j=i+1

  #     result=arr[j]-arr[i]

  #     if result==0:

  #       if arr[i] not in duplicate_numbers:

  #         duplicate_nuumbers.append(arr[i])

  #     print(duplicate_numbers)




 
