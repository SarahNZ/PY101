# or operator returns True if either operand 1 OR operand are true.
# So one operand can be truthy or both.
# And operator returns Truthy is both operands are True
# Exclusive Or (known as xor) returns True if exactly (or only) one of its
# operands are truthy

def xor(value1, value2):
    # returns True if exactly one of its arguments is truthy
    # Arg1 True, Arg2 False
    if value1 and not value2:
        return True
    # Arg1 False, Arg1 True
    elif not value1 and value2:
        return True
    # Arg1 True, Arg2 True
    # Arg1 False, Arg2 False
    else:
        return False

### Examples ###
# Only one argument is True (the other is False)
print(xor(5, 0) == True)
print(xor(False, True) == True)

# Both operands are True, so want xor to return False
print(xor(1, 1) == False)
print(xor(True, True) == False)