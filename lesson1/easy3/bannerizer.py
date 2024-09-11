def print_in_box(string):
    # Compute how many hypens or spaces to print
    padding = len(string) + 2
    horizontal_rule = f"+{padding * '-'}+"
    empty_line = f"|{padding * ' '}|"
    # Print '+' and then '-' length of the string + 2 times and '+' at end
    print(horizontal_rule)
    print(empty_line)
    print(f'| {string} |')
    print(empty_line)
    print(horizontal_rule)

print_in_box('')
print_in_box('To boldly go where no one has gone before.')