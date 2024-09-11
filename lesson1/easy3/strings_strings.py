def stringy(length):
    if length >= 1:  
        # Initialize the result string
        result = ''    
        # Return string of 1s and 0s, starting with a 1
        for idx in range(length):
            if idx % 2 == 0:
                result += '1'
            else:
                result += '0'
            # Provided solution was more concise
            # digit = '1' if idx % 2 == 0 else '0'
            # result += digit
        return result

# Should all print True
print(stringy(0) == None)
print(stringy(1) == '1')     
print(stringy(2) == '10')
print(stringy(3) == '101')   
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True