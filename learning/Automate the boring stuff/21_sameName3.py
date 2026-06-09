'''
усі змінні - або локальні, або глобальні
'''

def spam():
    global eggs
    eggs = 'spam'   # це глобальна змінна

def bacon():
    eggs = 'bacon'  # це локальна
    print(eggs)

def ham():
    print(eggs)     # це глобальна

def my_var():
    bacon()         # тут локальна bacon
    print(eggs)     # це глобальна spam

eggs = 42           # це глобальна змінна
spam()
print(eggs)         # spam

bacon()             # bacon
print(eggs)         # spam

my_var()            # bacon     spam
print(eggs)         # spam

'''
Розділимо на глобальні та локальні

eggs = 42 (рядок внизу) — глобальна.

spam() оголошує global eggs, тобто всередині spam() вона змінює глобальну.

bacon() створює локальну змінну eggs = 'bacon', бо там нема global eggs.

ham() читає eggs, і якщо немає локальної, бере глобальну.

my_var() викликає bacon(), де є локальна і вона друкується,
але після закінчення функції вона зникає,
і далі print(eggs) в my_var() показує глобальну.
'''