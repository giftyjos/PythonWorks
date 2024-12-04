arr=[10,20,30,40,2,3]

# list comprehension
# dicitionary comprehension

# {10:100,20:400,,,,}

result={}#empty dictionary
for num in arr:#num=10

    square=num**2 #sqaure=100

    result[num]=square
print(result)

# ........nxt qn..# dicitionary comprehension

arr=[10,20,30,40,2,3]
# result={key:value iteration condition}
result={num:num**3 for num in  arr}

print(result)

# ...nxt qn odd numbers...

arr=[10,20,30,40,2,3,7,8,9]

# frequency of numbers

# even_square={num:num**2 for num in arr if num%2==0}

# print(even_squares)
# odd_cubes={num:num**3 for num in arr if num%2!=0}

# print(odd_cubes)

# result={key:value iteration condition}

# result={num:num**3 for num in arr}
# print(result)
# 



#  ....frequency count nxt qn....

arr=[10,20,30,40,2,3,7,8,9,10,30]

# frequency of numbers

frequency_count={num:arr.count(num) for num in arr}

print(frequency_count)