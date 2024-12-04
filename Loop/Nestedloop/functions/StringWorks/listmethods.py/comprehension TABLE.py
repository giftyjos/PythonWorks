# list comprehension

# arr=[2,3,4,5,6,7]

# # reference=[return loop condition]

# square=[num**3 for  num in arr]

# cubes=[]



arr=[2,3,4,5,6,7]

# return iteration condition

# even numbers

add_ten=[num+10 for num in arr]

print(add_ten)

odd_numbers=[num for num in arr if num%2!=0]

print(odd_numbers)

even_numbers=[num for num in arr if num%2==0]

print(even_numbers)

num_gt_five=[num for num in arr if num>5]

print(num_gt_five)


# return a new list num+1 if num>5 else num-1




# return a new list num+1 with vowels

# words starting with vowels
text=["apple","iphone","orange","potatto","tomatto"]

vowel_words=[w for w in text if w[0]in ['a','e','i','o','u']]

print(vowel_words)

consonat_words=[w for w in text if w[0] not in ['a','e','i','o','u']]

print(consonat_words)

# longest word

long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]

print(longest_words)

# 

# -----TABLE-----
# collection name        define           is duplicates allowed?        insertion order preserved?   mutable         methods

# list                   [] or ()            yes                            yes                      yes           append(),insert(),index(),sort(),extend(),copy(),reverse(),count()

# tuple                   ()                  yes                            yes                     no                 index(),count()

# set                   set ()                no                            no                       yes  add(obj),intersection(),union(),difference(),remove(),issubset(),issuperset(),symmetric_difference(),update()


# dictionary             {}              duplicate keys are not allowed                            yes               get(),pop(),keys(),values(),items()




# ........list and dictionary are important collections......