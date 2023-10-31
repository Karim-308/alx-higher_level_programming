#!/usr/bin/python3
import sys

def is_valid(queens, col):
    row = len(queens)
    for q_row, q_col in enumerate(queens):
        if q_col == col or \
           q_col - q_row == col - row or \
           q_col + q_row == col + row:
            return False
    return True

def n_queens(n, board=[]):
    if len(board) == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_valid(board, col):
            n_queens(n, board + [col])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens(n)
