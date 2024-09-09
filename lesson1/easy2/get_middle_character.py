def center_of(string):
    # Check the string is not empty
    if string:
        # Compute the length of the string
        length = len(string)    #19
        # Check if the length of the string is odd
        # Find the middle index (by integer dividing by 2)
        # Note: / will return a float, which we don't want
        # Also don't need to use import math math.floor() to round down
        middle_index = length // 2
        # Find the middle character
        middle_char = string[middle_index]
        if length % 2 == 1:
            # Return the middle character
            return middle_char
        # Else if the string is even
        else:
            # Find the middle index minus 1
            second_middle_index = middle_index - 1
            # Find the middle plus 1 character
            second_middle_char = string[second_middle_index]
            # Return middle and second to middle chars
            return second_middle_char + middle_char

    else:
        print("String is empty. Can't compute middle character")

### Test Cases
print(center_of(''))      # Empty string (/)
print(f"This is the middle character, '{center_of(' ')}'") # Blank string (/)
print(center_of('x') == "x")                               # True
print(center_of('sb') == 'sb')                             # True
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True