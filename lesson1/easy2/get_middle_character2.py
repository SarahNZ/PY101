def center_of(string):
    if len(string) % 2 == 1:
        center_index = len(string) // 2
        return string[center_index]
    else:
        left_index = len(string) // 2 - 1
        # Use string splicing to extract two characters starting at the left_
        # index 
        return string[left_index:left_index + 2]

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