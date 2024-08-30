'''Note: Couldn't use str.casefold() method to convert strings to uppercase.
It actually converts all the characters in the string to lower case). 
'''
name = input("What is your name? ")

if name.endswith('!'):
    print(f"HELLO {name.upper()}! WHY ARE WE YELLING?") 
else:
    print(f"Hello {name}.")