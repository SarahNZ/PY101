# LANGUAGE = 'en'
LANGUAGE = 'es'

import json

def prompt(key):
    message = messages(key, LANGUAGE)
    print(f' => {message}')

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def invalid_number(number_str):
    # try/except statement catches the ValueError exception when number_str
    # can't be converted to an integer. The end result is that invalid_number
    # returns False if number_str can be converted to an integer, True if it
    # cannot
    try:
        float(number_str)
    except ValueError:
        return True
    
    return False

# Now 'MESSAGES' contains the contents of the JSON file as a Python dictionary
# or list

def calculation():
    # Ask the user for the first number
    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    # Ask the user for the second number
    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    # Ask the user for an operation to perform
    prompt('operation')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        operation = input()

    # Perform the operation on the two numbers
    match operation:
        case '1':   
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    output = round(output, 2)

    # Print the result to the terminal
    print(f"The result is: {output}\n")

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# print(messages('welcome'))
# or can do
print(messages('welcome'))

while True:
    calculation()
    # Ask the user if they want to perform another calculation
    prompt(messages('repeat_operation'))
    answer = input()
    # if answer and answer[0].lower() != 'y':
    # Not using above line of code as yes is 't' in Spanish
    if answer != '1':
        break

# Test Cases
# Addition
# 0, 0 == 0
# 1, 2 == 3
# -1, -2 == -3
# 0.4, 0.6 => ValueError: invalid literal for int() with base 10: '0.4'

# Subtraction
# 0, 0 == 0
# 1, 2 == -1
# 2, 1 == 1
# -1, -2 == 1
# 0.4, 0.6 => Get error ValueError: invalid literal for int() with base 10: 
# ... '0.4'

# Multiplication
# 0, 0 == 0
# 1, 2 == 2
# -1, -2 == 2
# 1, -2 == -2
# 0.4, 0.6 x

# Division
# 0, 0 => ZeroDivisionError: division by zero
# 0, 1 = 0.0
# 1, 0 = ZeroDivisionError: division by zero
# 1, 2 == 0.5
# -1, -2 == 2
# 0.4, 0.6 x