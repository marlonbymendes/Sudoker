from grid import Grid
from copy import deepcopy

def setup_grid():
    rows = 5
    columns = 5
    cells = [1, 2, 3]
    grid = Grid(rows, columns, cells)
    return deepcopy(grid)

def test_get_row():
    grid = setup_grid()

    grid.set_cell(2, 2, 3)
    expected = [1, 1, 3, 1, 1]
    assert grid.get_row(2) == expected

def test_constructor():
    grid = setup_grid()
    expected = [[1 for i in range(5)] for i in range(5)]
    assert grid.grid == expected
