# tester.py
from sudokuSolver import Solver
import random


def sudokuSolver_tester():
    """
    gets a random 9x9 sudoku board to test on the solver
    (will only work on 9x9). will only allow 17 numbers on the
    board.

    Returns:
        list of lists: new random sudoku board (9x9)
    """
    newboard = []
    board_size = 81
    max_take_away = 64

    for x in range(0, 9):
        newboard.append([] * 9)

    for i in range(0, 9):
        for s in newboard:
            s.append(random.randint(1, 9))

    for t in random.sample(range(board_size), max_take_away):
        newboard[t//9][t % 9] = 0

    return newboard


test = Solver(sudokuSolver_tester())
test.show_board()
