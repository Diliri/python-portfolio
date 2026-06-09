'''
Інструкція global всередині функції змінює глобальну змінну
'''
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)