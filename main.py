from grid import *
from sudoku import Sudoku

g = Grid(5, 5, ['a', 'b'])
print(g)
print(g.cells)

s = Sudoku()
print(s)
print(s.dimension)
