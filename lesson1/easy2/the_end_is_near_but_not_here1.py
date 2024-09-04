# Return middle word in a phrase/sentence
# Note: Words are any sequence of non-blank characters

def middle_word(words):
        # Convert string into a list of words (split at space) after removing
        # leading and trailing spaces
        words_list = words.strip().split()
        # print(words_list)
        number_of_words = len(words_list)
        if number_of_words > 2:
            if (number_of_words % 2 != 0):
                    # What is the index of the middle word
                    index_of_middle_word = round(number_of_words // 2)
                    # Return the second to last word in the list
                    return words_list[index_of_middle_word]
            else:
                  return ("Can't find middle word as there is an even number "
                          "of words in the list. Needs to be an odd number")
        else:
            return ("Can't find middle word as there needs to be at least 3"
                " words in the list")

# These examples should print True
# Odd number of words, so can find and print middle word
print(middle_word("Launch School rocks!") == "School")  # Odd number of words
print(middle_word("sarah says hi") == "says")  # 5 words, odd

# Even number of words, so can't find the middle word
print(middle_word("last word") == "Can't find middle word as there needs to "
                                  "be at least 3 words in the list") # 2 words

# Edge cases
print(middle_word("") == "Can't find middle word as there needs to "
                         "be at least 3 words in the list") # empty string
print(middle_word(" ") == "Can't find middle word as there needs to "
                          "be at least 3 words in the list") # blank string
print(middle_word("one") == "Can't find middle word as there needs to "
                            "be at least 3 words in the list") # 1 word
print(middle_word("Launch School is great!") == "Can't find middle word as " 
                            "there is an even number of words in the list. "
                            "Needs to be an odd number") # 4 words/even