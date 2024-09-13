def is_double_number(number):
    # Convert int to a string
    number_string = str(number)
    # Compute length of the number string
    length = len(number_string)
    # Check if length is even
    if length % 2 == 0:
        # Split string in half and see if two halves are equal
        # Find center of the string (using integer division)
        center = length // 2
        first_half = number_string[:center]
        second_half = number_string[center:]
        # If two halves equal
        if first_half == second_half:
            return True
    return False

def twice(number):
    # if number is a double_number
    if is_double_number(number):
        return number
    else:
        return number * 2
    
# Examples
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

