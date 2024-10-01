# Question 1

for num in range(1,11):
    print(f"{'-' * num}The Flintstones Rock!")

# Question 2
def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print( factors(-1))

# Question 4
import math

print(math.isclose(0.3 + 0.6, 0.9))

# Question 5
nan_value = float("nan")
print(math.isnan(nan_value))

# Question 10
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
print(id(a))
print(id(b))
print(id(c))
