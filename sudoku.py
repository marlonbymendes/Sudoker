from grid import Grid

class Sudoku(Grid):
    _dimension = 9
    _valid_cells = [i for i in range(_dimension + 1)]
    _quadrant_size = _dimension // 3
    _solved_valid_cells = set([i for i in range(1, _dimension + 1)])
    _quadrant_dimension = 3
        
    def __init__(self, table=None):
        if table is None:
            super().__init__(Sudoku._dimension, Sudoku._dimension, Sudoku._valid_cells)
        else:
            super().__init__(table=table)

    @property
    def dimension(self):
        return Sudoku._dimension

    # Both columns and rows are considered "lines"
    def is_line_solved(self, line):
        return set(line) == self._solved_valid_cells

    def is_solved(self):
        for i in range(self.dimension):
            if not self.is_line_solved(self.get_row(i)):
                return False
            if not self.is_line_solved(self.get_column(i)):
                return False
        for i in range(Sudoku._quadrant_dimension):
            for j in range(Sudoku._quadrant_dimension):
                quadrant = self.get_quadrant_as_list(i, j)
                if not self.is_line_solved(quadrant):
                    return False
        return True

    def get_quadrant_as_list(self, row, column):
        i_start = row * 3
        j_start = column * 3
        quadrant = []
        
        for i in range(i_start, i_start + 3):
            for j in range(j_start, j_start + 3):
                quadrant.append(self.get_cell(i, j))
        return quadrant
