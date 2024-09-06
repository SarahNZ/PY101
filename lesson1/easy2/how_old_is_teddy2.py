# Further Exploration - My Solution

import random

name = input("Please enter your name: ")

 # If no name is entered, use 'Teddy'
if not name:           
    name = 'Teddy'      

# Randomly generate an age between 20 and 100 years inclusive
age = random.randint(20, 100)

print(f"{name} is {age} years old!")