# enumerate function
collection = ['a', 'b', 'c']
for index, element in enumerate(collection):
    print(f"Index: {index}, Element: {element}")
'''
Output:
Index: 0, Element: a
Index: 1, Element: b
Index: 2, Element: c
'''
# zip function
numbers = [1,2,3,4,5]
letters = ['a', 'b', 'c']
combined = list(zip(numbers, letters))
print(combined)
# [(1, 'a'), (2, 'b'), (3, 'c')]