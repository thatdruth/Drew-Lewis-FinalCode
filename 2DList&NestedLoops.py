
number_grid = [
    [1, 2, 3], #Row 0
    [4, 5, 6], #Row 1
    [7, 8, 9], #Row 2
    [0] # Row 3
]

print(number_grid[0][1])
print(number_grid[2][2])


#Nested For Loop

for row in number_grid:
    print(row)
    for col in row:
        print(col)