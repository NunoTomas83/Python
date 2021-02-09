""" Script to use several python list functions"""

my_list = [5, 2, 9, 1]

second_list = list(range(5))

print("Length :", len(my_list))
print("1st Index :", my_list[0])
print("1st 3 Values :", my_list[0:3])
print("9 in List :", 9 in my_list)
print("Index for 2 :", my_list.index(2))
print("How Many 2s :", my_list.count(2))

my_list.remove(1)
my_list.pop(0)
my_list.insert(0, 10)

my_list.sort()

print("Sorted : {}".format(my_list))

my_list.reverse()

print("Sorted : {}".format(my_list))

