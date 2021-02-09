""" Script to determine which school should a child go """

age = int(input("Please insert your age: "))

# Handle if age < 5
if age < 5:
    print("Too young to school")

# Special output just for age 5
elif age == 5:
    print("Go to Kindergarden")
    #Since a number is the result for ages 6 - 17 we can check them all
    # with 1 condition
    # Use calculation to limit the conditions checked

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))

# Handle everyone else
else:
    print("Go to College")