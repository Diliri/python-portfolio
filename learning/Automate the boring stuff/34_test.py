list_in_list = [[0,1], [2,3], [5,9]]
print(list_in_list[0][1]) # 1
print(list_in_list[1][0])   # 2

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]

'''
def heart(grid):
    for x in range(0,9):
        y = 0
        while y < 6:
            print(grid[x][y], end = ' ')
            y += 1
        print()
'''

def heart(grid):
    for y in range(6):         # стовпці
        for x in range(9):     # рядки
            print(grid[x][y], end=' ')
        print()  # новий рядок після кожного стовпця

heart(grid) # це повертає сердечко на 90 градусів