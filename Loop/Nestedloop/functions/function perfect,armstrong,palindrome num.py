# is_perfect number

def is_perfect(number):
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    return sum_divisors == number

# Example usage
num = 28
if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")


# is_armstrong_number(number)

def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over digits
    num_str = str(num)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum is equal to the original number
    return armstrong_sum == num

    number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


    
    
# def is_palindrome_number(number):
    # Convert the number to a string
    str_number = str(number)
    # Check if the string is equal to its reverse
    return str_number == str_number[::-1]

# Test the function

    



