# Гра "відгадай число"
import random
secretNumber = random.randint(1, 20)
print('Мною загадане число від 1 до 20.')
print('Спробуйте його відгадати.')

# Надати гравцю 6 спроб для відгадування числа
for guessesTaken in range(1, 7):
    print('Ваш варіант: ')
    guess = int(input())

    if guess < secretNumber:
        print('Запропоноване число менше задуманого.')
    elif guess > secretNumber:
        print('Запропоноване число більше задуманого.')
    else:
        break   # Ви вгадали!

if guess == secretNumber:
    print('Вірно! Кількість спроб: ' + str(guessesTaken))
else:
    print('Ні. Було задумане число ' + str(secretNumber))