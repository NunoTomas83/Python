"""
Convert word to unicode and back to word again

# Computers assign characters with a number known as a Unicode A-Z have the numbers 65-90 and a-z 97-122

"""

norm_string = input("Entre a string to hide: ")
secret_string = ""

#convert to secret message
for char in norm_string:
    secret_string += str(ord(char))
print("Secret message is: {}". format(secret_string))

#convert back to normal
norm_string = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code))
print("Original message: ", norm_string)
