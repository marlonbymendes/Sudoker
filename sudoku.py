from grid import Grid

class Sudoku(Grid):
    __dimension = 9
    __valid_cells = [i for i in range(dimension + 1)]
    __solved_valid_cells = set([i for i in range(1, dimension + 1)])


    def __init__(self):
        super().__init__(Sudoku.__dimension, Sudoku.__dimension, Sudoku.__valid_cells)

    # Both columns and rows are considered "lines"
    def is_line_solved(self, line):
        return set(line) == __solved_valid_cells

    def is_solved(self):
        for i in range(Sudoku.__dimension):
            if !is_line_solved(self.get_row(i)):
                return False
            if !is_line_solved(self.get_column(i)):
                return False
        return True
