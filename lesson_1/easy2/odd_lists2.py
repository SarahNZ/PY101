'''
Further Exploration Question:
Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.

Try to solve this differently from the exercise described above.
'''
def return_nth_element(lst):
    return lst[::nth_element]

# Examples hard-coded for nth_element = 4
nth_element = 4
print(return_nth_element([2, 3, 4, 5, 6]) == [2, 6])     # True
print(return_nth_element([1, 2, 3, 4]) == [1])           # True
print(return_nth_element(["abc", "def"]) == ['abc'])     # True
print(return_nth_element([123]) == [123])                # True
print(return_nth_element([]) == [])                      # True