""" Section 9 - Strings
Convert word to unicode and back to word again

# Computers assign characters with a number known as a Unicode A-Z have the numbers 65-90 and a-z 97-122

"""

norm_string = input("Entre a string to hide: ")
secret_string = ""

#convert to secret message
for char in norm_string:

    #The 23 is that the number won't pass to 3 digits so that when converting back to normal we can still
    #cycle 2 digits at a time

    secret_string += str(ord(char-23))
print("Secret message is: {}". format(secret_string))

#convert back to normal
norm_string = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code+23))
print("Original message: ", norm_string)
