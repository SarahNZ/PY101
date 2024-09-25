def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True    
    return False

prompt("Welcome to Mortgage Calculator!")

while True:
    prompt("What's the loan amount?")

    amount = input()
    while invalid_number(amount):
        prompt("Must enter a positive number")
        amount = input()
    prompt("What is the interest rate?")
    prompt("(Example: 5 for 5% or 2.5 for 2.5%)")
     
    interest_rate = input()
    while invalid_number(interest_rate):
        prompt("Must enter a positive number")
        interest_rate = input()

    prompt("What is the loan duration (in years)?")
    years = input()

    while invalid_number(years):
        prompt("Must enter a positive number")
        years = input()

    annual_interest_rate = float(interest_rate) / 100
    monthly_interest_rate = annual_interest_rate / 12
    months = float(years) * 12
    loan_amount = float(amount)

    # Interest Calculation Formula
    monthly_payment = loan_amount * (
        monthly_interest_rate / 
            (1 - (1 + monthly_interest_rate) ** (-months))
    )
    # Output (monthly payment in dollar and cents value. E.g. $123.45)
    print(f'Your monthly payment is ${monthly_payment:.2f}.')

    prompt("Another calculation?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break

'''
# Test Cases
Test Case   loan_amt    APR     loan_dur_years  months    monthly_payment
2           1           0       0               1         $1.00
3           1000000     100     100             12        $83333.33
4           5000000     0.25    0               24        $208876.30
5           5000000     200     0               24        $854466.87
'''