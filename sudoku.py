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

    def unique_in_line(self, element, line):
        return line.count(element) == 1

    def unique_in_row(self, i, j):
        row = self.get_row(i)
        cell = self.get_cell(i, j)
        return self.unique_in_line(cell, row)

    def unique_in_column(self, i, j):
        column = self.get_column(j)
        cell = self.get_cell(i, j)
        return self.unique_in_line(cell, column)

    def unique_in_quadrant(self, i, j):
        quadrant_pos = self.get_cell_quadrant(i, j)
        quadrant = self.get_quadrant_as_list(quadrant_pos[0], quadrant_pos[1])
        cell = self.get_cell(i, j)
        return self.unique_in_line(cell, quadrant)

    # returns True if cell is unique in row, column and quadrant
    def unique_in_cross(self, i, j):
        l_unique = [self.unique_in_row, self.unique_in_column, self.unique_in_quadrant]
        unique = True
        for function in l_unique:
            unique = unique and function(i, j)
        return unique

    def get_cell_quadrant(self, i, j):
        quadrant = (i // 3, j // 3)
        return quadrant

    def unique_in_row(self, row, column):
        element = self.get_cell(row, column)
        line_count = self.get_row(row).count(element)
        return line_count == 1

    # Valid positions: (0, 0), (0, 1), (0, 2), (1, 0), ... (2, 2)
    def get_quadrant_as_list(self, row, column):
        i_start = row * 3
        j_start = column * 3
        quadrant = []
        
        for i in range(i_start, i_start + 3):
            for j in range(j_start, j_start + 3):
                quadrant.append(self.get_cell(i, j))
        return quadrant

    def get_candidates(self, i, j):
        cell = self.get_cell(i, j)
        candidates = set()
        if cell == 0:
            quadrant_pos = self.get_cell_quadrant(i, j)
            row, column, quadrant = (self.get_row(i),
                                     self.get_column(j),
                                     self.get_quadrant_as_list(quadrant_pos[0], quadrant_pos[1]))
            lines = [row, column, quadrant]
            used = set()
            for line in lines:
                for cell in line:
                    used.add(cell)
            candidates = self._solved_valid_cells - used
        else:
            candidates.add(cell)
        return candidates
