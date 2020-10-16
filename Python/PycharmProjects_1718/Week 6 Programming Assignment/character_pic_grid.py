grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for y in range(len(grid[0])):  # [y] is the assigned y place in the list [grid], formerly the x place
    for x in range(len(grid)):  # [x] is the assigned x place in the list [grid], formerly the y place
        print(grid[x][y], end="")  # this flips them so the picture flips
    print("")  # helps shifts to a new line
