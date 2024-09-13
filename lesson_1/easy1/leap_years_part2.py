'''Requirements limited to the following countries to limit scope. For other
countries leap year is unknown

United Kingdom of Great Britain and Northern Island   GB  1752    
British colonies 1752 (limited to)
    # New Zealand (NZ)           
    # Australia (AU)
    # Canada (CA)
Japan  JP  1873  
Korea  KP  1896 
China  CN  1912 

Iso codes sourced from wikipedia (20-08-2024)
https://en.wikipedia.org/wiki/List_of_ISO_3166_country
'''

def is_leap_year(year, country):
    match country:
        case 'GB'| 'NZ'| 'AU'| 'CA':
            start_year_gregorian_calendar = 1752
        case 'JP':
            start_year_gregorian_calendar = 1873
        case 'KP':
            start_year_gregorian_calendar = 1896
        case 'CN':
            start_year_gregorian_calendar = 1912
        

    # Use Gregorian calendar
    if year > start_year_gregorian_calendar:             
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return year % 4 == 0
    else:
        # Use Julian calendar before that
        return year % 4 == 0
    
# Test Cases for method accepting two arguments
# Test Cases for non-Leap year during use of the Julian calendar (for all   
# countries)
print(is_leap_year(1, 'NZ') == False)
print(is_leap_year(1, 'GB') == False)
print(is_leap_year(1, 'AU') == False)
print(is_leap_year(1, 'CA') == False)
print(is_leap_year(1, 'JP') == False)
print(is_leap_year(1, 'KP') == False)
print(is_leap_year(1, 'CN') == False)

# Test Cases for Leap year during use of the Gregorian calendar (for all   
# countries)
print(is_leap_year(2024, 'NZ') == True)
print(is_leap_year(2024, 'GB') == True)
print(is_leap_year(2024, 'AU') == True)
print(is_leap_year(2024, 'CA') == True)
print(is_leap_year(2024, 'JP') == True)
print(is_leap_year(2024, 'KP') == True)
print(is_leap_year(2024, 'CN') == True)

# Need to add test cases for boundaries of each country case