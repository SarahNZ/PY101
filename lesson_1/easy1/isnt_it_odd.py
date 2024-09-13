'''
# P: Understand the problem: Mental Model #
input: function takes one integer arg
output: return bool
        True when number's absolute value is odd
        False if otherwise

# Clarifying Questions
1. What is a number's absolute value?
The absolute value (or modulus) of a real number is the non-negative value
without regard to it's sign. So we disregard the sign.
2. Is 0 an integer? Or do integers start from 1? Is 0 an even integer? 
0 is an integer and is a neutral integer, neither positive nor negative.
0 is an even integer
3. Can integers be negative? Yes, they can be positive, negative or zero

# E: Examples/Test Cases:
Test Case #     Input   Expected Output     Manual Algorithm Output
1               0       False               False
2               1       True                True
3               2       False               False
-1              -1      True                True

Edge Cases/Error Handling:
N/A

# D: Data Structure
N/A

# A: Algorithm

1. Pass one integer argument to a function called is_it_odd
2. Determine the absolute value of the integer
3. Check if the integer is odd by dividing it by two and seeing it if has a
remainder (using modulus)
4. If the remainder is not zero return True
5. Otherwise return False (if the remainder is zero)

# C: Code (with intent)
'''
def is_it_odd(int):
    absolute_value = abs(int)
    remainder = absolute_value % 2
    if remainder != 0: # Solution given was remainder == 1 is odd
        return True
    else:
        return False

# Tests
print(is_it_odd(0))
print(is_it_odd(1))
print(is_it_odd(2))
print(is_it_odd(-1))

# Given solution is
def is_odd(number):
    return abs(number) % 2 ==1