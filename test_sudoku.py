from sudoku import Sudoku

class SudokuConstants:
    dimension = 9
    quadrant_size = 3
    valid_cells = [i for i in range(dimension + 1)]
    unsolved_sudoku = [[1, 2, 3, 1, 2, 3, 1, 2, 3],
		       [4, 5, 6, 4, 5, 6, 4, 5, 6],
		       [7, 8, 9, 7, 8, 9, 7, 8, 9],
		       [1, 2, 3, 1, 2, 3, 1, 2, 3],
		       [4, 5, 6, 4, 5, 6, 4, 5, 6],
		       [7, 8, 9, 7, 8, 9, 7, 8, 9],
		       [1, 2, 3, 1, 2, 3, 1, 2, 3],
		       [4, 5, 6, 4, 5, 6, 4, 5, 6],
		       [7, 8, 9, 7, 8, 9, 7, 8, 9]]

    solved_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    unsolved_sudoku2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9]]



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


def test_get_valid_qudrant():
    s = Sudoku(sConstants.unsolved_sudoku)
    expected = [i for i in range(1, 10)]
    for i in range(sConstants.quadrant_size):
        for j in range(sConstants.quadrant_size):
            quadrant = s.get_quadrant_as_list(i, j)
            assert quadrant == expected

def test_get_invalid_quadrant():
    s = Sudoku(sConstants.unsolved_sudoku)
    try:
        quadrant = s.get_quadrant_as_list(sConstants.quadrant_size, sConstants.quadrant_size)
    except IndexError:
        pass

def test_solved_sudoku():
    s = Sudoku(sConstants.solved_sudoku)
    assert s.is_solved()

def test_unsolved_sudoku():
    s = Sudoku(sConstants.unsolved_sudoku2)
    assert not s.is_solved()

def test_unique_in_cross():
    s = Sudoku(sConstants.solved_sudoku)
    for i in range(sConstants.dimension):
        for j in range(sConstants.dimension):
            assert s.unique_in_cross(i, j)

def test_not_unique_in_cross():
    s = Sudoku(sConstants.unsolved_sudoku2)
    assert not s.unique_in_cross(6, 0)
