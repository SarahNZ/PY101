'''
Launch School's solution which used a slightly different module to calculate
the current year than i did in solution 1
'''
# Import date class from datetime module
from datetime import datetime as dt # Can then use the alias, dt

# Ask user to input current age and planned retirement age
current_age = int(input("What is your age? "))  
retirement_age = int(input("At what age would you like to retire? "))

### Compute the current year
current_year = dt.now().year

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

'''
There are 2 ways to compute the current year:
1. 
from datetime import date
current_year = date.today().year
or
2.
from datetime import datetime
current_year = datetime.now().year
'''
