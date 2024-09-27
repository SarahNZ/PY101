# Exercise 2
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(str1.endswith("!"))   # True
print(str2.endswith("!"))   # False

# Exercise 3
famous_words = "seven years ago..."
text = "Four score and "

message1 = text + famous_words
message2 = f"{text}{famous_words}"


print(message1)
print(message2)

# Exercise 4
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

print(munsters_description.capitalize())

# Exercise 5
munsters_description = "The Munsters are creepy and spooky."

print(munsters_description.swapcase())

# Exercise 6
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print('Dino' in str1)
print('Dino' in str2)

# Exercise 7
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.append('Dino')
print(flintstones)

# Exercise 8
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])
print(flintstones)

# Exercise 9
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
print(advice.split("house")[0])
print(advice.split("house")[1])

# Exercise 10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("important", "urgent"))