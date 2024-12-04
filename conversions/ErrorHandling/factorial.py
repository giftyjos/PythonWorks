# def factorial(num):

#     fact=1

def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from the user
number = int(input("Enter a non-negative integer: "))
print(f"The factorial of {number} is {factorial_iterative(number)}.")
