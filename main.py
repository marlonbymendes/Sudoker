from grid import *

rows = 9
columns = 9
cells = [i for i in range(1, 10)]

grid = Grid(rows, columns, cells)
print(grid)

grid.set_cell(4, 4, 7)
grid.set_cell(2, 2, 3)
print(grid)

print(grid.get_row(2))
print(grid.get_row(4))
