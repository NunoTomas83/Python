"""Several function regarding list comprehensions"""

multiples = []
for x in range(1, 11):
    multiples.append(x * 7)

print(multiples)
print("--------------------------------")

multi = [x * 7 for x in range(1, 11)]
print(multi)
print("--------------------------------")
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lens = [len(y) for y in languages]
print(lens)
print("--------------------------------")
z = [j for j in range(0, 101) if j % 3 == 0]
print(z)
print("--------------------------------")

def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []
