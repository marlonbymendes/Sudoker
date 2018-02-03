from sudoku import Sudoku

class SudokuConstants:
    dimension = 9
    valid_cells = [i for i in range(dimension + 1)]

sConstants = SudokuConstants()

def test_sudoku_default_constructor():
    s = Sudoku()

    for i in range(sConstants.dimension):
        for j in range(sConstants.dimension):
            cell = s.get_cell(i, j)
            if cell not in sConstants.valid_cells:
                raise ValueError

def test_set_cell_invalid_value():
    s = Sudoku()
    try:
        s.set_cell(4, 3, 10)
    except ValueError:
        pass

def test_set_cell_valid_values():
    s = Sudoku()
    for cell in sConstants.valid_cells:
        s.set_cell(8, 8, cell)

def test_set_cell_outside_grid():
    s = Sudoku()
    try:
        s.set_cell(9, 9, 1)
    except IndexError:
        pass

