""" Prints a # made Xmas Tree given a height """

# how tall is the tree

        #
       ###
      #####
        #

height = int(input("How tall is the tree "))

spaces = height - 1
hashes = 1
stump_space = height - 1

while height != 0:
    for i in range(spaces):
        print(" ", end="")
    for i in range(hashes):
        print("#", end="")
    print()  # issue a new line because of the stump
    spaces -= 1
    hashes += 2
    height -=1

for i in range(stump_space):
    print(" ", end="")
print("#")


