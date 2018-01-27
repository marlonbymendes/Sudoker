class Grid():

    def __init__(self, rows, columns, cells):
        self._cells = cells
        self._rows = rows
        self._columns = columns
        self._grid = [[cells[0] for i in range(columns)] for i in range(rows)]

    @property
    def cells(self):
        return self._cells

    @property
    def grid(self):
        return self._grid

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def get_row(self, index):
        return self.grid[index]

    def get_column(self, index):
        col = []
        for row in self.grid:
            col.append(row[index])
        return col

    def inside_grid(self, row, column):
        return (row >= 0 and row < self.rows) and \
                (column >= 0 and column < self.columns)

    def set_cell(self, row, column, value):
        if value in self.cells:
            if self.inside_grid(row, column):
                self._grid[row][column] = value
            else:
                raise IndexError('Row or column not inside grid bounds.')
        else:
            raise ValueError('Value is not a valid cell.')

    def __str__(self):
        output = ''
        for row in self.grid:
            for cell in row:
                output += (str(cell) + ' ')
            output += '\n'
        return output
