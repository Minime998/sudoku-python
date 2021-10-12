# sudokuSolver.py

class Solver(object):
    def __init__(self, board):
        self.board = board

    def show_board(self):
        """
        Used to show sudoku board.

        Returns:
            None: N/A
        """

        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -|")
            for y in range(len(self.board[0])):
                if y % 3 == 0 and y != 0:
                    print(" | ", end="")
                if y == 8:
                    print(str(self.board[i][y])+"|")
                else:
                    print(str(self.board[i][y]) + " ", end="")

        return None
