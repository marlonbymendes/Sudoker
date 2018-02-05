from sudoku import Sudoku
from random import randint

class SudokuBuilder:

    def __init__(self):
        self._sudoku = Sudoku()
        self._set_free_cells()

    @property
    def grid(self):
        return self._sudoku.grid

    def _set_free_cells(self):
        self._free_i = 0
        self._free_j = 0

    def _update_free_cell(self):
        dimension = self._sudoku.dimension
        j_start = self._free_j
        for i in range(self._free_i, dimension):
            for j in range(j_start, dimension):
                if self._sudoku.get_cell(i, j) == 0:
                    self._free_i = i
                    self._free_j = j
                    return
            j_start = 0
        raise IndexError('There are no more free cells.')

    def generate_random_cell(self):
        return randint(1, self._sudoku.dimension)

    def _fill_free_cell(self):
        i = self._free_i
        j = self._free_j
        assert self._sudoku.get_cell(i, j) == 0
        sudoku = self._sudoku

        checked = set()
        while len(checked) < sudoku.dimension:
            value = self.generate_random_cell()
            checked.add(value)
            sudoku.set_cell(i, j, value)
            if sudoku.unique_in_cross(i, j):
                self._update_free_cell()
                return
        raise ValueError('Can\'t set a valid cell in this position.')

    def _fill_all_free_cells(self):
        while True:
            try:
                self._fill_free_cell()
            except IndexError:
                break
            except ValueError:
                self._reset()

    def _reset_free_cells(self):
        self._free_i = 0
        self._free_j = 0

    def _reset(self):
        self._reset_free_cells()
        self._sudoku.clear()

    def generate_sudoku(self):
        self._reset()
        self._fill_all_free_cells()
        return self._sudoku
