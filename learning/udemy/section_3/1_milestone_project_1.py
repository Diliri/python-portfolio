def add(collection):
    title = input('Please, enter a name of a new film: ')
    director1 = input('Please, enter a director\'s name of a new film: ')
    release_year = input('Please, enter a year of a new film: ')
    collection.append({
        'name': title,
        'director': director1,
        'year': release_year
    })


def printed_out(collection):
    for film in collection:
        print(f"{film['name']} ({film['year']}), directed by {film['director']}")


def finding_a_film(collection):
    user_input = input('Please, enter a word for finding an information about film: ')
    finded_films = []
    for film in collection:
        if (user_input.lower() in film['name'].lower()
            or user_input.lower() in film['director'].lower()
            or user_input in film['year']):
            finded_films.append(film)
    # print(finded_films) це виведе список словників — не дуже красиво.
    if finded_films:
        for f in finded_films:
            print(f"{f['name']} ({f['year']}), directed by {f['director']}")
    else:
        print("No films found.")


films = [{
    'name': 'The Matrix',
    'director': 'Wachowskis',
    'year': '1994'
}]

MENU_PROMPT = '''You could
add a new film to a collection (print 'add'),
look into a collection (print 'look'),
find some films (print 'find'),
or print 'q' to quit.'''

print(MENU_PROMPT)
user_input = input("Enter command (add/look/find/q): ")

while user_input != 'q':
    if user_input == 'add':
        add(films)
    elif user_input == 'look':
        printed_out(films)
    elif user_input == 'find':
        finding_a_film(films)
    else:
        print("Please, enter 'add', 'look', 'find' or 'q'.")

    user_input = input("Enter command (add/look/find/q): ")
