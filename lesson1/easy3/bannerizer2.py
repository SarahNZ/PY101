# max_width argument is optional
def print_in_box(string, max_width=None):
    # Compute how many hypens or spaces to print
    box_width = len(string) + 2
    if (max_width == None) or (box_width <= max_width):
        horizontal_rule = f"+{box_width * '-'}+"
        empty_line = f"|{box_width * ' '}|"
    else:
        # Truncate the string to the max_width
        # Can use string slicing specifying the end index 
        # I.e. string[start:end] E.g. string[:10] 
        # truncates astring to the first 10 characters. Starts at the start 
        # index (incl) and ends at the end index (exclusive)
        string = string[:max_width]
        # Make the box borders shorter too
        horizontal_rule = f"+{(max_width + 2) * '-'}+"
        empty_line = f"|{(max_width + 2) * ' '}|"
    print(horizontal_rule)
    print(empty_line)
    print(f'| {string} |')
    print(empty_line)
    print(horizontal_rule)

print_in_box('')
print_in_box('To boldly go where no one has gone before.')
print_in_box('To boldly go where no one has gone before.', 20)

# This Python tutorial was really useful: 
# https://tutorpython.com/truncate-python-string/

# Note: Another way to truncate a string is to import textwrap module and use
# wrapped_text = textwrap.shorten(string, width=max_width)