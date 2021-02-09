"""Acronim: The user enters a string and it creates an acronim"""

orig_string = input("Please enter a string: ")
orig_string = orig_string.upper()
list_of_words = orig_string.split()
final_word = ""

for word in list_of_words:
    # print(word[0], end="")
    final_word = final_word + word[0]

print("The word is: {}".format(final_word))



