class Grid():

    def __init__(self, rows, columns, cells):
        self.rows = rows
        self.columns = columns
        self.cells = cells
        self.grid = [[cells[0] for i in range(columns)] for i in range(rows)]

    def get_cells(self):
        return self.cells

    def get_grid(self):
        return self.grid

    def get_row_number(self):
        return self.rows

    def get_column_number(self):
        return self.columns

    def get_row(self, index):
        return self.get_grid()[index]

    def get_column(self, index):
        col = []
        grid = self.get_grid()
        for row in grid:
            col.append(row[index])
        return col

    def inside_grid(self, row, column):
        return (row >= 0 and row < self.get_row_number()) and \
                (column >= 0 and column < self.get_column_number())

    def set_cell(self, row, column, value):
        if value in self.get_cells():
            if self.inside_grid(row, column):
                grid = self.get_grid()
                grid[row][column] = value
            else:
                raise IndexError('Row or column not inside grid bounds.')
        else:
            raise ValueError('Value is not a valid cell.')

    def __str__(self):
        grid = self.get_grid()
        output = ''
        for row in grid:
            for cell in row:
                output += (str(cell) + ' ')
            output += '\n'
        return output
