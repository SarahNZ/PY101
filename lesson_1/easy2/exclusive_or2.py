# More concise solutions provided by Launch School

def xor(value1, value2):
    if (value1 and not value2) or (value2 and not value1):
        return True
    
    return False

def xor2(value1, value2):
    return bool((value1 and not value2) or (value2 and not value1))

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

print(xor2(5, 0) == True)
print(xor2(False, True) == True)
print(xor2(1, 1) == False)
print(xor2(True, True) == False)

# or and 'and' are called short-circuit operators because the second operand is
# not evaluated if its value is not needed. xor is not a short-circuit
# operation.

# Example of when xor may be needed?
# If the person is a customer and hasn't received a discount yet, then offer
# them a discount