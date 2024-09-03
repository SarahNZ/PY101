# Prompt user for two positive numbers (floating point)
# Don't need to validate the input
num1 = float(input("==> Enter the first number:\n"))
num2 = float(input("==> Enter the second number:\n"))


def floating_point_arithmetic(num1, num2):
    # Addition
    sum = num1 + num2
    print(f"==> {num1} + {num2} = {sum}")

    # Subtraction
    difference = num1 - num2
    print(f"==> {num1} - {num2} = {difference}")

    # Product
    product = num1 * num2
    print(f"==> {num1} * {num2} = {product}")

    # Quotient
    if num2 != 0:
        quotient = num1 / num2
        print(f"==> {num1} / {num2} = {quotient}")
    else:
        print("Unable to compute quotient, as can't divide by 0")

    # Floor quotient (is like integer division)
    if num2 != 0:
        floor_quotient = num1 // num2
        print(f"==> {num1} // {num2} = {floor_quotient}")
    else:
        print("Unable to compute floor quotient, as can't divide by 0")

    # Remainder (use % operator)
    if num2 != 0:
        remainder = num1 % num2
        print(f"==> {num1} % {num2} = {remainder}")
    else:
        print("Unable to compute remainder, as can't divide by 0")

    # Power (use ** operator)
    power = num1 ** num2
    print(f"==> {num1} ** {num2} = {power}")

floating_point_arithmetic(num1, num2)

'''
### Hard-coded input tests ***
floating_point_arithmetic(3.141529, 2.718282)
print(f'Test passed for sum: {sum == 5.859811}')
print(f'Test passed for subraction: {difference == 0.42324699999999993}')
print(f'Test passed for product: {product == 8.539561733178}')
print(f'Test passed for quotient: {quotient == 1.1557038600115808}')
print(f'Test passed for floor quotient: {remainder == 1.0}')
print(f'Test passed for remainder {remainder == 0.42324699999999993}')
print(f'Test passed for power {power == 22.45792517468373}')


### Edge-case Tests ***
# floating_point_arithmetic(0, 0)
# floating_point_arithmetic(1, 2)
# floating_point_arithmetic(-1, -2)

'''
