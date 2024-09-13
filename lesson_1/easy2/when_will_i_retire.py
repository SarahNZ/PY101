'''
# Example
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
'''
# Import date class from datetime module
from datetime import date

# Ask user to input current age and planned retirement age
current_age = int(input("What is your age? "))  
retirement_age = int(input("At what age would you like to retire? "))

### Compute the current year
# Compute today's date
today = date.today()

# Compute current year
current_year = today.year

# Compute the number of years left before retirement
years_of_work_left = retirement_age - current_age

# Compute the year that they will retire
retirement_year = current_year + years_of_work_left

# Output
print(f'It\'s {current_year}. You will retire in {retirement_year}.')
print(f'You have only {years_of_work_left} years of work to go!')

# Tests - the following should all print True
if current_age == 30 and retirement_age == 70:
    print(current_year == 2024)
    print(years_of_work_left == 40)
    print(retirement_year == 2064)