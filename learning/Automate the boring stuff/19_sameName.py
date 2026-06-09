'''
треба уникати повторення локальних та глобальних імен.
Хоча з технічної точки зору в Пайтон - це можливо зробити
'''
def spam():
    eggs = 'spam local'
    print(eggs) # виводиться рядок 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # виводиться рядок 'bacon local'
    spam()
    print(eggs) # виводиться рядок 'bacon local'

eggs = 'global'
bacon()
print(eggs) # виводиться рядок 'global'

'''
bacon local
spam local
bacon local
global
'''