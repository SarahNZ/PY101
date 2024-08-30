def greetings(name, status):
    # Combine 2 or more elements in the list to make a string of a person's 
    # full name
    full_name = ' '.join(name)
    # Get the title and occupation values frpm the dictionary
    title = status.get("title")
    occupation = status.get("occupation")
    return (f'Hello, {full_name}! Nice to have a {title} {occupation} around.')

# Given solution puts all the code in the formatted string
def greetings2(name, status):
        return (f"Hello, {' '.join(name)}! Nice to have a "
                f"{status['title']} {status['occupation']} around.")

# Tests
greeting = greetings2(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)

'''
# Example
Input:
["John", "Q", "Doe"], {"title": "Master", "occupation": "Plumber"}

Output: 
Hello, John Q Doe! Nice to have a Master Plumber around.
'''