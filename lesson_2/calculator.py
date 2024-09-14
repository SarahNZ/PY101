print('Welcome to the Calculator!')

# Ask the user for the first number
number1 = input("What's the first number? ")

# Ask the user for the second number
number2 = input("What's the second number? ")

print(f'{number1} {number2}')

# Ask the user for an operation to perform
operation = input('What operation would you like to perform?\n1) Add '
                  '2) Subtract 3) Multiply 4) Divide\n')

# Perform the operation on the two numbers
if operation == '1':    # '1' represents addition
    output = int(number1) + int(number2)
elif operation == '2':
    output = int(number1) - int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
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
# 0.4, 0.6 => Get error ValueError: invalid literal for int() with base 10: '0.4'

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