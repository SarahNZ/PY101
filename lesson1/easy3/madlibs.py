'''
Example:
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
'''
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
print()

# Print the user input into this story
print(f'Do you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!')
print(f'The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.')
print(f'The {noun} {adjective} {verb}s up to Joe\'s {adjective} turtle.')