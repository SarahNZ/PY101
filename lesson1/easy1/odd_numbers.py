'''
# input
all_numbers = list(range(1, 100, 2))
# print(all_numbers)

# algorithm
for number in all_numbers:
    if number % 2 == 1:
        # output
        print(number)

# Bonus Question
1. Modify the code above to add step by 2 to the range
'''
# input
start = int(input("Enter integer to start at: "))
finish = int(input("Enter integer to finish at: ")) + 1

# algorithm
for number in range(start, finish, 2):
        print(number)