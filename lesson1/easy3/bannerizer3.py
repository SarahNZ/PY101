'''
Note: Can't use textwrap, because that can only add symbols to the start
of each line, not the end.

Do this exercise later on, as need to get through this module soon.

Solution ideas:
# Split the string into words using possibly str.split() which will split the
string at whitespace.
# The loop through each word
    # If the word can't be added to the current line, add padding, and a pipe
    # and move to the next line
'''
# Word wrap messages
def print_in_box(string, max_width=None):
    # Compute how many hypens or spaces to print
    box_width = len(string) + 2
    if (max_width == None) or (box_width <= max_width):
        horizontal_rule = f"+{box_width * '-'}+"
        empty_line = f"|{box_width * ' '}|"
    else:
        # Word wrap the string to fit in the box
        # TODO wrapped_text = ?
        # Make the box borders shorter too
        horizontal_rule = f"+{(max_width + 2) * '-'}+"
        empty_line = f"|{(max_width + 2) * ' '}|"
    print(horizontal_rule)
    print(empty_line)
    print(f'| {string} |')
    print(empty_line)
    print(horizontal_rule)

# print_in_box('')
# print_in_box('To boldly go where no one has gone before.')
print_in_box('To boldly go where no one has gone before.', 20)