# Nested loops
# Create a matrix of given dimensions using a nested loops

rows = 3
columns = 2
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(f'{i} - {j}')
    matrix.append(row)

print(matrix)
'''
output

[
['0 - 0', '0 - 1'],
['1 - 0', '1 - 1'],
['2 - 0', '2 - 1']
]
'''