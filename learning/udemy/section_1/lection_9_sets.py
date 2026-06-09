''' Sets in python '''

# they don't hold order and don't contain duplicate elements

art_friends = {'Rolf', "Ann"}
science_friends = {'Jen', "Charlie"}

art_friends.add('Jen')
print(art_friends)  # {'Ann', 'Jen', 'Rolf'} NO ORDER !!!

art_friends.add('Jen')
print(art_friends)  # {'Ann', 'Jen', 'Rolf'} NO DUPLiCATES !!!

art_friends.remove('Jen')
print(art_friends)  # {'Ann', 'Rolf'} removed !!!