def multiply(num1, num2):
    return num1 * num2

def power(number, n):
    # Powers less than 0 are out of scope
    if n >= 0:
        result = number
        for i in range(1, n):
            result = multiply(result, number)
        return result
    else:
        print("Power needs to be greater or equal to 0. Negative powers not "
              "supported")

# Examples
print(multiply(5, 3) == 15)  # True

print(power(0, 0) == 0)   # True
print(power(1, 0) == 1)   # True
print(power(1, 1) == 1)   # True
print(power(2, 1) == 2)   # True
print(power(2, 2) == 4)   # True
print(power(2, 3) == 8)   # True
print(power(-8, 3) == - 512)  # True
print(power(8, -3))  # Prints unsupported message