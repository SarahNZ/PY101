def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    # try/except statement catches the ValueError exception when number_str
    # can't be converted to an integer. The end result is that invalid_number
    # returns False if number_str can be converted to an integer, True if it
    # cannot
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

print('Welcome to the Calculator!')

# Ask the user for the first number
prompt("What's the first number? ")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

# Ask the user for the second number
prompt("What's the second number? ")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

# print(f'{number1} {number2}')

# Ask the user for an operation to perform
prompt('What operation would you like to perform?\n1) Add '
                  '2) Subtract 3) Multiply 4) Divide\n')
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

# Perform the operation on the two numbers
match operation:
    case '1':   
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

# Print the result to the terminal
print(f"The result is: {output}")

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