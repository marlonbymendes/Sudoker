from sudoku_solver import SudokuSolver

class SolverConstants:

    table = [[0, 0, 0, 0, 0, 3, 0, 0, 6],
             [0, 0, 3, 5, 0, 0, 0, 8, 0],
             [1, 0, 0, 6, 4, 0, 0, 7, 3],
             [5, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 4, 8, 7, 0, 0, 0],
             [0, 8, 0, 0, 0, 0, 0, 0, 9],
             [4, 3, 0, 0, 2, 5, 0, 0, 7],
             [0, 5, 0, 0, 0, 6, 2, 0, 0],
             [7, 0, 0, 1, 0, 0, 0, 0, 0],
            ]

    easy_sudoku = [[0, 0, 0, 0, 5, 6, 0, 0, 2],
	           [6, 0, 9, 7, 0, 2, 0, 0, 0],
	           [0, 2, 7, 0, 0, 0, 0, 9, 0],
	           [0, 6, 0, 0, 0, 9, 0, 0, 8],
	           [5, 0, 0, 0, 0, 0, 3, 0, 4],
	           [0, 1, 0, 0, 0, 7, 0, 0, 9],
	           [0, 8, 6, 0, 0, 0, 0, 3, 0],
	           [9, 0, 3, 2, 0, 1, 0, 0, 0],
	           [0, 0, 0, 0, 9, 3, 0, 0, 6]]


    solver = SudokuSolver(table)

ss = SolverConstants().solver

def test_find_candidates_in_row():
    row = 6
    value = 1
    expected = [2, 6]

    assert ss.find_value_candidates_in_row(row, value) == expected

def test_find_candidates_in_column():
    column = 8
    value = 8
    expected = [3, 7, 8]

    assert ss.find_value_candidates_in_column(column, value) == expected

def test_find_candidates_in_quadrant():
    quadrant = (0, 2)
    value = 2
    expected = [(0, 7), (1, 8)]

    assert ss.find_value_candidates_in_quadrant(quadrant, value) == expected

def test_solve_easy_sudoku():
    ss = SudokuSolver(SolverConstants.easy_sudoku)
    sudoku = ss.solve_sudoku()
    assert sudoku.is_solved()
