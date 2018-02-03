from grid import Grid
from copy import deepcopy

def setup_grid():
    rows = 5
    columns = 5
    cells = [1, 2, 3]
    grid = Grid(rows, columns, cells)
    return deepcopy(grid)

class Table:
    def __init__(self):
        self.table = [[1, 2, 1, 3], [3, 2, 1, 4], [1, 1, 1, 5]]
        self.rows = 3
        self.columns = 4
        self.cells = [1, 2, 3, 4, 5]

def test_get_row():
    grid = setup_grid()

    grid.set_cell(2, 2, 3)
    expected = [1, 1, 3, 1, 1]
    assert grid.get_row(2) == expected

def test_constructor():
    grid = setup_grid()
    expected = [[1 for i in range(5)] for i in range(5)]
    assert grid.grid == expected

def test_get_cell():
    grid = setup_grid()
    expected = 1
    return grid.get_cell(3, 3) == expected

def test_set_cell_correctly():
    grid = setup_grid()
    cell_value = 3
    grid.set_cell(2, 3, cell_value)

def test_set_cell_invalid_value():
    grid = setup_grid()
    cell_value = 9
    try:
        grid.set_cell(2, 3, cell_value)
    except ValueError:
        pass

def test_set_cell_outside_bounds():
    grid = setup_grid()
    cell_value = 1
    try:
        grid.set_cell(10, 10, cell_value)
    except IndexError:
        pass

def test_grid_str():
    grid = setup_grid()
    expected = '1 1 1 1 1 \n' * 5
    assert str(grid) == expected

def test_constructor_from_table_rows():
    table = Table()
    grid = Grid(table=table.table)
    assert table.rows == grid.rows

def test_constructor_from_table_columns():
    table = Table()
    grid = Grid(table=table.table)
    assert table.columns == grid.columns

def test_constructor_from_nom_rectangular_table():
    table = [[1, 2, 3, 4], [1, 2, 3], [1, 2, 3, 4]]
    try:
        grid = Grid(table=table)
    except ValueError:
        pass

def test_cells_from_talbe_constructor():
    table = Table()
    grid = Grid(table=table.table)
    expected = table.cells
    assert grid.cells == expected

def test_clear():
    table = Table()
    grid = Grid(table=table.table)
    grid.clear()
    for i in range(grid.rows):
        for j in range(grid.columns):
            assert grid.get_cell(i, j) == table.cells[0]
