def crunch(string):
        new_string = ''
        last_char = ''
        for char in string:
            if char != last_char:
                new_string += char
            last_char = char

        return new_string

print(crunch('a') == 'a')
print(crunch('') == '')
print(crunch('abc') == 'abc')
print(crunch('gggggggg') == 'g')
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')