'''
Trying a new solution that uses two methods liked the given solution for the
Further Exploration problem

Test Cases
# numbers = "1 2 3 4 5", sum, expected result = 15
# numbers = "1 2 3 4 5", product, expected result = 720

# numbers = "1", sum, expected result = 1
# numbers = "1", product, expected result = 1

# numbers = "10 2 15 100", sum, expected result = 127
# numbers = "10 2 15 100", product, expected result = 30000
'''

# Initialize variables
prompt1 = "Please enter a space separated list of integers (greater than 0): "
prompt2 = 'Enter "s" to compute the sum, or "p" to compute the product: '

# Declare functions
def compute_sum(numbers):
    return sum(numbers)  # E.g. 3
    
def compute_product(numbers):
    result = 1
    for num in numbers:
        result *= num   # E.g. 2
    return result

### User input (remove leading and trailing whitespace) ###
string_of_numbers_with_spaces = (input(prompt1).strip())        # E.g. '2'
operation = input(prompt2).strip()          # E.g.'s'

# Modify input from a string of numbers to a list of integers
# 1. Split the string at the spaces and create a list of comma delimited strings
list_of_number_strings_without_spaces = string_of_numbers_with_spaces.split(' ')

# 2. Convert the number strings to integers
numbers = [int(num) for num in list_of_number_strings_without_spaces]

### Output ###

# Call the sum or product methods
if operation == 's':
    print(f'The sum of the integers you entered, '
          f'{string_of_numbers_with_spaces}, is {compute_sum(numbers)}.')
elif operation == 'p':
    print(f'The product of the integers you entered, '
          f'{string_of_numbers_with_spaces}, is {compute_product(numbers)}.')
else:
    print("Unknown operation. Please run the program again and enter s or p")