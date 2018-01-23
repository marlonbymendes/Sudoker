from copy import deepcopy


class Grid:

    def __init__(self, rows=1, columns=1):
        self.__grid = [[]]

    def get_grid(self):
        return deepcopy(self.__grid())
