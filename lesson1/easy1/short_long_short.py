def short_long_short(string1, string2):
    # Calculate the length of both strings and compare the strings to see 
    # which one is longer
    if len(string1) > len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1

### Test Cases ###
print(short_long_short('abc', 'defgh'))
print(short_long_short('abcde', 'fgh'))
print(short_long_short('', 'xyz'))

'''
# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
'''