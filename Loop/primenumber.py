
# exclude(1,number)
# .example
# number is 7 . then 7 factors are  1 and 7 

#  1  and  7 are exculded  2 3 4 5 6 these numbers are divide by 7 aanekil prime number aavila . alenki prime number aan




number=int(input("enter number:"))

is_prime=True

# factors of number(1,number) 

for i  in range(2,number): # i=2 3 4 5 6 

    if number%i==0:

        is_prime=False

        break

print(is_prime)

# leapyear
# Armstrong
# GCD 
# LCM
# PRIME
# Datastructures and Algorithms(array,stack,queue,linkedlist,tree,graph)
