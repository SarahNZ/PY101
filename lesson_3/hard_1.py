# Question 1
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return 
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# Question 2

dictionary = {'first': [1]}
# References the original list
num_list = dictionary['first']
# To copy the list and change the copy without changing the original list
# num_list = dictionary['first'].copy()
# Use list slicing to return a new list
num_list = dictionary["first"][:]
# Modifies the original list as num_list references the original list
num_list.append(2)

print(num_list)
print(dictionary)