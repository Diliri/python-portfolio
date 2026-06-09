def spam():
    print(eggs)     # ERROR!
    # UnboundLocalError: variable 'eggs'
    # referenced before assignment
    eggs = 'spam local'

eggs = 'global'
spam()

'''
", line 6, in <module>
    spam()
    ~~~~^^
  File "/home/DianaListen/Automate the boring stuff/22_sameName4.py
", line 2, in spam
    print(eggs)     # ERROR!
          ^^^^
UnboundLocalError: cannot access local variable 'eggs' where it is
not associated with a value
'''