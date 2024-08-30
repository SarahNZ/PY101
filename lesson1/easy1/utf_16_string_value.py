def utf16_value(string):
    # Determine the UTF-16 string value of the string,
    # which is the sum of the UTF-16 values of every char in the string
    sum_ = 0
    for char in string:
        # Use ord(char) to determine the UTF-16 value of a character
        sum_ += ord(char)
    return sum_  # Check that the return statement is at the correct tab 
                 # alignment. I.e. Vertically aligned with the start of the
                 # for statement, not inside the for statement!!

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"      # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)