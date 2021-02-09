"""Script to elaborate list and print only data in odd positions"""

def skip_elements(elements):
    even_list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            even_list.append(element)
    return even_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

"""
def skip_elements(elements):
    return [i for i in elements if elements.index(i)%2 == 0]

"""
