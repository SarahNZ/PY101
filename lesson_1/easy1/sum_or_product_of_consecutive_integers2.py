'''
My original solution to the Further Exploration problem manually checking for
spaces, but only copes with single digit numbers

Input 
# Prompt user to enter a list of space separated integers greater than 0 
(save as a list of numbers and change spaces to ,)
# Prompt the user to specify if they want to determine the sum or the product of 
all the numbers between 1 and the int (inclusive) - save operation abbreviation

Algorithm
# Convert the string of numbers to a list of integers
# Create a variable, result to hold the sum or product
# If operation is sum, initizalise result to 0, then loop through all the 
numbers in the list and add them to the result (a new integer).
# If the operation is product, initialise result to 1, then loop through all 
the numbers in the list and multiply them by the result

# Output
Print the result

Test Cases
# numbers = "1 2 3 4 5", sum, expected result = 15
# numbers = "1", sum, expected result = 1
# numbers = "1 2 3 4 5", product, expected result = 720
# numbers = "1", product, expected result = 1

'''

string_of_numbers = (input("Please enter a list of integers greater than 0 " 
                           "separated by spaces: "))
operation_abbreviation = input('Enter "s" to compute the sum, or "p" to '
                               'compute the product: ')
print() # Adds a line space between the input and the output

# Convert the string of numbers to a list of integers
list_of_number_strings = list(string_of_numbers)
numbers = []
for num in list_of_number_strings:
    if num != ' ':
        num = int(num)  # Convert the string number to an integer
                        # Add the integer to a new list
        numbers.append(num)

result = 0

if operation_abbreviation == "s":
    operation = "sum"
    result = sum(numbers)
elif operation_abbreviation == 'p':
    operation = "product"
    result = 1
    for num in numbers:
        result *= num
else:
    print("Unknown operation. You needed to specify an s or p for the"
          "computation operation. Please run the program again.")

print(f"The {operation} of the integers you entered, {numbers}, is {result}.")