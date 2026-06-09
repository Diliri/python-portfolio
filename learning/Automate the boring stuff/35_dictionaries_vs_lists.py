# dictionaries vs lists
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'cats', 'moose']
print(spam == bacon)    # False

eggs = {'name': 'Zophie', 'species': 'cat'}
ham = {'species': 'cat', 'name': 'Zophie'}
print(eggs == ham)      # True