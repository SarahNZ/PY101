'''
def oddities(lst):
    result = []
    # Find every 2nd item in the original list and add to a
    # new list (not sure how). Maybe i + 2?
    for idx in range(len(lst)):   # Need to iterate through the index of the
        if idx % 2 == 0:          # list, not the list items themselves
            result.append(lst[idx])
    return result

Given bonus question solution (which I didn't know) using Python's list slicing
This allows me to start from the first element and skip every second element
Slicing format is list[start:stop:step]
    start: The beginning index of the slice
    stop: The end index of the slice (exclusive)
    step: The interval between elements

In list[::2] no start or stop is provided, so it defaults to the beginning of 
list and the end of the list. 2 is provided as the step, so every second
element is taken
'''

def oddities(lst):
    return lst[::2]

# Examples
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True