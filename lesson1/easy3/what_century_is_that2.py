def century(year):
    if 1 <= year <= 99:
        century = "1"
    else:
        string_year = str(year)
        # Split string into two parts
        # Part 1 is all the digits except the last 2
        first_digits = string_year[:-2]
        # Part 2 is the last 2 digits
        last_2_digits = string_year[-2:]
        if last_2_digits == "00":
            century = first_digits
        else:
            century = int(first_digits) + 1
    # Return century and suffix as one string
    return (f'{century}{suffix(century)}')

def suffix(positive_integer):
    # Convert the positive integer into a string
    number_string = str(positive_integer)
    # Get the last 2 digits of the century
    if len(number_string) > 2:
        number_string = number_string[-2:]
    # Convert to an integer
    number = int(number_string)
    match number:
        case 1 | 21 | 31 | 41 | 51 | 61 | 71 | 81 | 91:
            return "st"
        case 2 | 22 | 32 | 42 | 52 | 62 | 72 | 82 | 92:
            return "nd"
        case 3 | 23 | 33 | 43 | 53 | 63 | 73 | 83 | 93:
            return "rd"
        case _:
            return "th"

# Examples
print(century(1965) == "20th")  
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1) == "1st")
print(century(99) == "1st")
print(century(100) == "1st")
print(century(101) == "2nd")
print(century(199) == "2nd")
print(century(256) == "3rd")            # True 
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # False
print(century(1127) == "12th")          # False
print(century(11201) == "113th")        # False