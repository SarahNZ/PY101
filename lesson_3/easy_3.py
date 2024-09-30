# Question 1
numbers = [1, 2, 3, 4]
print(f'Original List: {numbers}')

numbers.clear()
print(f'Updated List: {numbers}')

# Question 2
result = [1, 2, 3] + [4, 5]
print(result)   # [1, 2, 3, 4, 5]

# Question 5
def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid2(color):
    return color in ["blue", "green"]

print(is_color_valid2("blue"))
print(is_color_valid2("pink"))