def clean_up(text):
    clean_text = ''
    # Go through the string character by character and add each character to
    # the new string if it is an alphabetic character
    for idx, char in enumerate(text):
        # If char is alphabetic add to clean_message
        if char.isalpha():
            clean_text += char
        # Else if the index is not 0 and the last char was not a space, add a
        # space
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '
    return clean_text

# Example
print(clean_up("---what's my +*& line?") == " what s my line ") # True
print(clean_up("what") == "what") # True
print(clean_up("---") == " ") # True
# str.isalpha() doesn't work for strings that contain Unicode letters that
# aren't part of the ASCII character set
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")   # True
# If I want to exclude letters that aren't part of the ASCII character set I
# need to use if char.isalpha() and char.isascii() 

# I.e. def is_ascii_letter(char)
#          return char.isalpha() and char.isascii()

# I originally kept track of last_char, but decided to change to use the 
# solution provided which enumerates the index of the string and uses the
# Python built-in str[-1] functionality.