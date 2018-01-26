from grid import Grid

class Sudoku(Grid):
    _dimension = 9
    _valid_cells = [i for i in range(_dimension + 1)]
    _quadrant_size = _dimension // 3
    _solved_valid_cells = set([i for i in range(1, _dimension + 1)])

        
    def __init__(self):
        super().__init__(Sudoku._dimension, Sudoku._dimension, Sudoku._valid_cells)

    @property
    def dimension(self):
        return Sudoku._dimension

    # Both columns and rows are considered "lines"
    def is_line_solved(self, line):
        return set(line) == self._solved_valid_cells

    def is_solved(self):
        for i in range(self.dimension):
            if not is_line_solved(self.get_row(i)):
                return False
            if not is_line_solved(self.get_column(i)):
                return False
        return True
