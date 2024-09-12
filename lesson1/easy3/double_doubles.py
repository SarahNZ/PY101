def twice(number):
    # Convert number to a string
    number_string = str(number)
    # Easiest way to find the length of digits of an int is to convert it to
    # a string and use len(str)
    length = len(number_string)
    # Check if number is double number
    # If number is even length
    if length % 2 == 0:
    # Split the string in half and save the two halves as separate strings
    # The slice goes from the start (inclusive) to the stop (exclusive)
    # Use integer division (so I get integer result)
        first_half = number_string[:length//2]
        second_half = number_string[length//2:]
        if first_half == second_half:
            # The number is a double number, so return the original number
            return number
    # Not a double number, so return number x 2
    return number * 2

print(twice(334433) == 668866)          # True
print(twice(103103) == 103103)          # True
print(twice(7676) == 7676)              # True
print(twice(37) == 74)
print(twice(44) == 44) 
print(twice(444) == 888)                
print(twice(107) == 214) 
print(twice(3333) == 3333)   