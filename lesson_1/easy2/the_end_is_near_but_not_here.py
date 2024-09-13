# Return second to last word (in the string argument)
# Note: Words are any sequence of non-blank characters
# Assume that the input string will always contain at least two words

def penultimate(words):
    words_list = words.split()
    print(words_list)
    return words_list[-2]
    
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")