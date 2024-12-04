# read  number 15
# print fizz if num/by 3
# print buzz if num/by 5
# print fizzbuzz if num/by 15
# default invalid number



number=int(input("enter number"))

if number %3==0:

    print("FIZZ")

elif number %5==0:

    print("BUZZ")

elif number % 15==0:

        print("FizzBuzz")
else:

    print("invalid number")
    