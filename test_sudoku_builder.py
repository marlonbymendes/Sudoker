from sudoku_builder import SudokuBuilder

def test_generate_sudoku():
    sb = SudokuBuilder()
    s = sb.generate_sudoku()
    assert s.is_solved()
