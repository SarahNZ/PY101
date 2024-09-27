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