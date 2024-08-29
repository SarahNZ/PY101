'''
Trying a new solution that uses two methods liked the given solution. In my
original solution I didn't use 2 methods, but it did work

Test Cases
# numbers = "1 2 3 4 5", sum, expected result = 15
# numbers = "1 2 3 4 5", product, expected result = 720

# numbers = "1", sum, expected result = 1
# numbers = "1", product, expected result = 1

# numbers = "10 2 15 100", sum, expected result = 127
# numbers = "10 2 15 100", product, expected result = 30_000
'''

# Initialize variables
prompt1 = "Please enter an integer greater than 0: "
prompt2 = 'Enter "s" to compute the sum, or "p" to compute the product: '

# Declare functions
def compute_sum(number):
    return sum(range(1, number+1))  # E.g. 3
    
def compute_product(number):
    result = 1
    for num in range(1, number+1):
        result *= num   # E.g. 2
    return result

### User input ###
number = int(input(prompt1).strip())        # E.g. '2'
operation = input(prompt2).strip()          # E.g.'s'

### Output ###

# Call the sum or product methods
if operation == 's':
    print(f'The sum of the integers between 1 and {number} is '
          f'{compute_sum(number)}.')
elif operation == 'p':
    print(f'The product of the integers between 1 and {number} is '
          f'{compute_product(number)}.')
else:
    print("Unknown operation. Please run the program again and enter s or p")