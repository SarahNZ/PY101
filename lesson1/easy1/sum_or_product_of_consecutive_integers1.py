'''
A solution to the Further Exploration problem using Python's str.split(' ')
method:

Use Python's built-in string splitter at delimiter
str.split(' ')

Also use list_of_numbers = [int(element) for element in list_of_strings]
to convert the numbers which are of string type to numbers which are int type

And strip any leading or trailing spaces from text input using 
new_string = str.strip()

'''

### Test Cases ###
# numbers = "1 2 3 4 5", sum, expected result = 15
# numbers = "1", sum, expected result = 1
# numbers = "1 2 3 4 5", product, expected result = 720
# numbers = "1", product, expected result = 1

# Input (and remove leading or trailing whitespaces)
text = (input("Please enter a list of integers greater than 0 " 
                           "separated by spaces: ").strip())    # E.g. "1 2 3"
operation_abbreviation = input('Enter "s" to compute the sum, or "p" to '
                               'compute the product: ').strip()
print() # Adds a line space between the input and the output
print(text)
# Convert the space delimited string to a comma delimited list of numbers
list_of_strings = text.split(' ')
# print(list_of_strings)      # E.g. ['1', '2', '3']
list_of_numbers = [int(string) for string in list_of_strings]
# print(list_of_numbers)      # E.g. [1, 2, 3]

result = 0

if operation_abbreviation == "s":
    operation = "sum"
    result = sum(list_of_numbers)
elif operation_abbreviation == 'p':
    operation = "product"
    result = 1
    for num in list_of_numbers:
        result *= num
else:
    print("Unknown operation. You needed to specify an s or p for the"
          "computation operation. Please run the program again.")

print(f"The {operation} of the integers you entered, {list_of_numbers}, is "
      f"{result}.")