from sudoku_builder import SudokuBuilder
from timeit import default_timer

def function_execution_time(function):
    start = default_timer()
    result = function()
    end = default_timer()
    elapsed = (end - start)
    return (result, elapsed)

def measure_generate_sudoku_performance():
    sb = SudokuBuilder()
    RUNS = 100
    accumulated_time = 0.0

    for i in range(RUNS):
        result = function_execution_time(sb.generate_sudoku)
        accumulated_time += result[1]

    performance = accumulated_time / RUNS
    print('Avarage generate sudoku performance: {:.2f} s'.format(performance))

measure_generate_sudoku_performance()
