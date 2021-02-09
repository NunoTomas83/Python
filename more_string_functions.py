
samp_string = ("  This is a very important string  ")
letter_z = "z"

edit_string = samp_string.strip()
#print("Uppercase :", edit_string)
print("Uppercase :", edit_string.upper())
print("Lowercase :", edit_string.lower())
list_string = edit_string.split()
print("Words")
for i in list_string:
    print(i)
print("How many ts?", edit_string.count("t"))
print("String Index :", edit_string.find("string"))
print("Replace very :", edit_string.replace("very ", "kind of "))
print("Is \"z\" a letter or number :", letter_z.isalnum())
print("Is \"z\" a letter :", letter_z.isalpha())
print("Is \"z\" a number :", letter_z.isdigit())
print("Is \"z\" a space :", letter_z.isspace())
