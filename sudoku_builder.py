from sudoku import Sudoku
from random import randint

class SudokuBuilder:

    def __init__(self):
        self._sudoku = Sudoku()
        self._free_i = 0
        self._free_j = 0
        self._MAX_TRIES = 25

    @property
    def grid(self):
        return self._sudoku.grid

    def __update_free_cell(self):
        i = self._free_i
        j = self._free_j

        if i >= self._sudoku.dimension:
            raise ValueError

        j += 1
        if j == self._sudoku.dimension:
            j = 0
            i += 1

        self._free_i = i
        self._free_j = j

    def __set_free_cell(self, value):
        self._sudoku.set_cell(self._free_i, self._free_j, value)
        self.__update_free_cell()

    def __fill_free_cell(self):
        i = self._free_i
        j = self._free_j
        if not self._sudoku.inside_grid(i, j):
            raise IndexError

        tries = 0
        while True:
            value = randint(1, self._sudoku.dimension)
            tries += 1
            self._sudoku.set_cell(i, j, value)
            if self._sudoku.unique_in_cross(i, j):
                self.__set_free_cell(value)
                break
            if tries == self._MAX_TRIES:
                raise ValueError('Maximum number of tries reachead')

    def __fill_all_free_cells(self):
        while True:
            try:
                self.__fill_free_cell()
            except IndexError:
                break
            except ValueError:
                self.__reset()

    def __reset_free_cells(self):
        self._free_i = 0
        self._free_j = 0

    def __reset(self):
        self.__reset_free_cells()
        self._sudoku.clear()

    def generate_sudoku(self):
        self.__reset()
        self.__fill_all_free_cells()
        assert self._sudoku.is_solved()
        return self._sudoku
