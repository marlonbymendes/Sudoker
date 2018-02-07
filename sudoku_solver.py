from sudoku_builder import SudokuBuilder
from sudoku import Sudoku
from copy import deepcopy
from random import shuffle

class SudokuSolver():

    def __init__(self, table):
        self._sudoku = Sudoku(table)
        self._init_cell_order()

    def _init_cell_order(self):
        self._cell_order = []
        for i in range(self._sudoku.dimension):
            for j in range(self._sudoku.dimension):
                if self._sudoku.get_cell(i, j) == 0:
                    self._cell_order.append((i, j))
        shuffle(self._cell_order)
    
    def _solve_recursive(self, cell_at):
        if cell_at == len(self._cell_order):
            return True

        row, column = self._cell_order[cell_at]
        for i in range(1, self._sudoku.dimension + 1):
            self._sudoku.set_cell(row, column, i)
            if self._sudoku.unique_in_cross(row, column):
               if self._solve_recursive(cell_at + 1):
                   return True

        self._sudoku.set_cell(row, column, 0)
        return False

    # Searches for the first cell which has a unique valid value (1-9)
    # Stops searching if a solution was found
    def find_cell_solution(self):
        sudoku = self._sudoku
        for i in range(sudoku.dimension):
            for j in range(sudoku.dimension):
                if sudoku.get_cell(i, j) != 0:
                    continue

                candidates = sudoku.get_candidates(i, j)
                if len(candidates) == 1:
                    value = next(iter(candidates))
                    solution = (i, j, value)
                    return solution
        return None

    def find_and_set_solution(self):
        solution = self.find_cell_solution()
        if solution is not None:
            i, j, value = solution
            self._sudoku.set_cell(i, j, value)
        else:
            raise CellSolutionNotFound('There is no solution for any cell')

    def _init_and_run_recursive_solution(self):
        self._init_cell_order()
        self._solve_recursive(0)

    def solve_sudoku(self):
        while True:
            try:
                self.find_and_set_solution()
            except CellSolutionNotFound:
                if not self._sudoku.is_solved():
                    print('Starting recursive solution')
                    self._init_and_run_recursive_solution()
                break

        assert self._sudoku.is_solved()
        return self._sudoku

    # Find column positions for a given row that are possible solutions for the given value
    def find_value_candidates_in_row(self, row, value):
        sudoku = self._sudoku
        candidates = []
        value_row = sudoku.get_row(row)
        try:
            value_at = value_row.index(value)
            candidates.append(value_at)
        except ValueError:
            for j in range(sudoku.dimension):
                if sudoku.get_cell(row, j) != 0:
                    continue

                if value not in sudoku.get_column(j):
                    if value not in sudoku.get_quadrant_from_cell(row, j):
                        candidates.append(j)
        return candidates

    # Find row positions for a given column that are possible solutions for the given value
    def find_value_candidates_in_column(self, column, value):
        sudoku = self._sudoku
        candidates = []
        value_column = sudoku.get_column(column)
        try:
            value_at = value_column.index(value)
            candidates.append(value_at)
        except ValueError:
            for i in range(sudoku.dimension):
                if sudoku.get_cell(i, column) != 0:
                    continue

                if value not in sudoku.get_row(i):
                    if value not in sudoku.get_quadrant_from_cell(i, column):
                        candidates.append(i)
        return candidates

    # Find row positions for a given column that are possible solutions for the given value
    def find_value_candidates_in_quadrant(self, quadrant_pos, value):
        sudoku = self._sudoku
        candidates = []
        row, column = quadrant_pos
        if value in sudoku.get_quadrant_as_list(row, column):
            return candidates

        i_start = row * 3
        j_start = column * 3
        rows = []
        columns = []
        for i in range(i_start, i_start + 3):
            rows.append(sudoku.get_row(i))

        for j in range(j_start, j_start + 3):
            columns.append(sudoku.get_column(j))

        for i in range(3):
            for j in range(3):
                real_i, real_j = i_start + i, j_start + j

                if sudoku.get_cell(real_i, real_j) == 0 and \
                   value not in rows[i] and \
                   value not in columns[j]:
                       candidates.append((i_start + i, j_start + j))
        return candidates

class CellSolutionNotFound(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

