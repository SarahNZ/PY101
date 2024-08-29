'''
A solution to the original problem: 

Write a program that asks the user to enter an integer greater than 0, 
then asks whether the user wants to determine the sum or the product of all 
numbers between 1 and the entered integer, inclusive.

Input 
Prompt user to enter an integer greater than 0 (number)
Prompt the user to specify if they want to determine the sum or the product of 
all the numbers between 1 and the int (inclusive)

Algorithm
# Save integer as number
# Save chosen maths operation as string, operation
# Create a list of numbers between 1 and the chosen number, using range + 1
# Create a variable, result to hold the sum or product
# If operation is sum, initizalise result to 0, then loop through all the 
numbers in the list and add them to the result (a new integer).
# If the operation is product, initialise result to 1, then loop through all 
the numbers in the list and multiply them by the result

# Output
Print the result

Test Cases
# int = 5, [1, 2, 3, 4, 5], sum, expected result = 15 (/)
# int = 1, [1], sum,   expected result = 1
# int = 6, [1, 2, 3, 4, 5, 6], product, expected result = 720
# int = 1, [1], product, expected result = 1

'''

number = int(input("Please enter an integer greater than 0: "))
operation_abbreviation = input('Enter "s" to compute the sum, or "p" to '
                               'compute the product: ')
print() # Adds a line space between the input and the output

numbers = list(range(1, (number + 1)))
# print(numbers)
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

print(f"The {operation} of the integers between 1 and {number} is {result}.")