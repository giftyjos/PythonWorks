


arr=[100,200,300,400,500]

k=1

# rotate array k times[500,100,200,300,400]

# k=2[400,500,100,200,300]

for i in range (1,k+1):
    popped_element=arr.pop()#500

    arr.insert(0,popped_element)

print(arr)