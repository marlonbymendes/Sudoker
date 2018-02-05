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

class CellSolutionNotFound(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

