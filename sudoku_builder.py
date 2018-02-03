from sudoku import Sudoku
from random import randint
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)

class SudokuBuilder:

    def __init__(self):
        self._sudoku = Sudoku()
        self._free_i = 0
        self._free_j = 0
        self._free_cells_stack = []

    @property
    def grid(self):
        return self._sudoku.grid

    def __update_free_cell(self):
        i = self._free_i
        j = self._free_j
        #self._free_cells_stack.append((i, j))

        if i >= self._sudoku.dimension:
            raise ValueError

        j += 1
        if j == self._sudoku.dimension:
            j = 0
            i += 1

        self._free_i = i
        self._free_j = j

    def __degrade_free_cell(self):
        i = self._free_i
        j = self._free_j
        self._sudoku.set_cell(i, j, 0)

        top_free_cell = self._free_cells_stack.pop()
        self._free_i = top_free_cell[0]
        self._free_j = top_free_cell[1]

    def __fill_free_cell(self):
        i = self._free_i
        j = self._free_j
        logging.info('filling ({}, {})..'.format(i, j))
        sudoku = self._sudoku

        if not sudoku.inside_grid(i, j):
            raise IndexError

        checked = set()
        while len(checked) < sudoku.dimension:
            value = randint(1, sudoku.dimension)
            checked.add(value)
            sudoku.set_cell(i, j, value)
            if sudoku.unique_in_cross(i, j):
                self.__update_free_cell()
                return
        raise ValueError('Can\'t set a valid cell in this position.')

    def __fill_all_free_cells(self):
        while True:
            try:
                self.__fill_free_cell()
            except IndexError:
                break
            except ValueError:
                logging.info('Reseting builder')
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
        return self._sudoku
