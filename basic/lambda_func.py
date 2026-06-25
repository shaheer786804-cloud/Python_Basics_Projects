# Define the lambda function
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"

# Test the function
number = 7
print(f"The number {number} is {check_even_odd(number)}.")
