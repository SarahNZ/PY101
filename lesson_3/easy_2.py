# Question 1
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reversed_numbers_1 = numbers[::-1]
print(reversed_numbers_1)

reversed_numbers_2 = list(reversed(numbers))
print(reversed_numbers_2)

# Question 2
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# Question 3
print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

# Question 4
numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers)

# Question 5
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(isinstance(numbers, list))
print(isinstance(table, list))

# Question 6
title = "Flintstone Family Members"
print(title.center(40))

# Question 7
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))

# Question 8
ages = {
            'Herman': 32, 
            'Lily': 30, 
            'Grandpa': 402, 
            'Eddie': 10
}

word = 'Spot'

if word in ages:
    print(f"{word} is a key in the dictionary")
else:
    print(f'{word} is not a key in the dictionary')
# print(ages.get('Spot'))

for _ in ages.values():
    if _ == {word}:
        print(f"{word} is a value in the dictionary")
else:
        print(f"{word} is not a value in the dictionary")

# Question 9
additional_ages = {'Marilyn': 22, 'Spot': 237}

# ages['Marilyn'] = 22
# ages['Spot'] = 237

ages.update(additional_ages)
print(ages)