'''
My solution, which works
'''
def negative2(number):
    if number > 0:
        number -= 2 * number
    return number

# Given solution
def negative(number):
    return -abs(number)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True