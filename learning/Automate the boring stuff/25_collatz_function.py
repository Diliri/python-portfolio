# page 114 or 110/573

def collatz(number):
    if number % 2 == 0:     # якщо число ПАРНЕ
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

while True:
    try:
        i = input('Please, enter a positive integer for Collatz sequence: ')
        i = int(i)
        if i <= 0:
            raise ValueError("Number must be positive!")  # перевірка на додатність
        while i != 1:
            i = collatz(i)
        break
    # у циклі while потрібно переприсвоїти змінну i = collatz(i),
    # щоб i отримувало нове значення після кожної ітерації.
    except ValueError or TypeError:
        print("Invalid input! Please enter a positive integer.\n")

'''
Ні, твій try-блок не буде виконуватись знову автоматично.
В Python структура try/except відпрацьовує один раз:

Якщо все пройшло без помилки → програма просто йде далі.

Якщо була помилка → виконується except,
і після цього програма продовжує після блоку try/except,
але не повертається назад до try.
'''

