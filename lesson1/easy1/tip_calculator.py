'''
# input
- Prompt user for bill amount
- Prompt user for tip percentage
# algorithm
- Calculate tip amount
# output
- Print tip amount and bill amount
'''
# input
bill_amount = float(input("What is the bill? "))
tip_percentage = float(input("What is the tip percentage? "))

# algorithm
tip_amount = bill_amount * (tip_percentage/100)
total = bill_amount + tip_amount

#output
print(f'The tip is ${tip_amount:.2f}')
print(f'The total is ${total:.2f}')

'''
### Tests ###
# Test 1
bill_amount = 200
tip_percentage = 20
tip_amount = 40.00
total = 240.00

# Test 2
bill_amount = 20.50
tip_percentage = 15.4
tip_amount = 3.16
total = 23.66
'''