from grid import Grid


def debug(**kwargs):
    for k, v in kwargs.items():
	print(f'{k} = {v}')


class Sudoku(Grid):
    _dimension = 9
    quadrant_size = _dimension // 3
    valid_cells = [i for i in range(__dimension + 1)]
    solved_valid_cells = set([i for i in range(1, __dimension + 1)])

    @property
    def dimension(self):
	return self._dimension
        
    @dimension.setter
    def dimension(self, value):
	self._dimension = int(value)

    def __init__(self):
        super().__init__(Sudoku.dimension, Sudoku.dimension, Sudoku.valid_cells)

    # Both columns and rows are considered "lines"
    def is_line_solved(self, line):
        return set(line) == self.solved_valid_cells

    def is_solved(self):
        for i in range(self.dimension):
            if not is_line_solved(self.get_row(i)):
                return False
            if not is_line_solved(self.get_column(i)):
                return False
        return True

    def get_quadrant_as_list(self, row, column):
        i_start = row * __quadrant_size
        j_start = column * __quadrant_size

        debug(i=i_start, j=j_start)
        

sudoku = Sudoku()
f = sudoku.is_solved
