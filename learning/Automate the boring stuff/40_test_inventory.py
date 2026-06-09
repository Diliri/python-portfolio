# task 1
stuff = {'arrow': 12, 'golden coin': 42, 'rope': 1,
    'torch': 6, 'dagger': 1
    }

def displayInventory(inventory):
    print('inventory: ')
    total_items = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        total_items += value
    print('Total number of items: ', total_items)

displayInventory(stuff)

# task 2
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin',
                'ruby']

def addToInventory(inventory, addedItems):
    for el in addedItems:
        if el not in inventory:
            inventory.setdefault(el, 1)
        else:
            inventory[el] += 1

addToInventory(inventory=stuff, addedItems=dragonLoot)
displayInventory(stuff)


