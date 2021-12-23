testcases = [
    {
        'input': {
            "board": [
                [7, 8, 0, 4, 0, 0, 1, 2, 0],
                [6, 0, 0, 0, 7, 5, 0, 0, 9],
                [0, 0, 0, 6, 0, 1, 0, 7, 8],
                [0, 0, 7, 0, 4, 0, 2, 6, 0],
                [0, 0, 1, 0, 5, 0, 9, 3, 0],
                [9, 0, 4, 0, 6, 0, 0, 0, 5],
                [0, 7, 0, 3, 0, 0, 0, 1, 2],
                [1, 2, 0, 0, 0, 7, 4, 0, 0],
                [0, 4, 9, 2, 0, 6, 0, 0, 7]
            ]
        },
        'output': [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=solveSudoku,
    )


"""
from copy import deepcopy


def get_possible_number(board, i, j):
    possibility = [True] * 9
    for k in range(9):
        x, y = board[i][k], board[k][j]
        if x != 0:
            possibility[x - 1] = False
        if y != 0:
            possibility[y - 1] = False
    block_y = (i // 3) * 3
    block_x = (j // 3) * 3
    for bi in range(block_y, block_y+3):
        for bj in range(block_x, block_x+3):
            z = board[bi][bj]
            if z != 0:
                possibility[z - 1] = False
    return [i+1 for i in range(9) if possibility[i] is True]


def dfs(board):
    print('a')
    is_finished = True
    for i in range(1):
        for j in range(9):
            if board[i][j] == 0:
                is_finished = False
                pos = get_possible_number(board, i, j)
                print('b', i, j, pos)
                if len(pos) == 0:
                    print('c')
                    return
                for n in pos:
                    matrix = deepcopy(board)
                    matrix[i][j] = n
                    dfs(matrix)
    if is_finished:
        print('d', board)
        return board
    print('f')


def solveSudoku(board):
    result = dfs(board)
    print('e', result)
    return result
"""


def solveSudoku(board):
    solveHelper(board, 0, 0)
    return board


def solveHelper(board, i, j):
    if j == 9:
        i += 1
        j = 0
        if i == 9:
            return True
    if board[i][j] == 0:
        return guess_number(board, i, j)
    return solveHelper(board, i, j+1)


def guess_number(board, i, j):
    for n in range(1, 10):
        if valid_board(board, i, j, n):
            board[i][j] = n
            if solveHelper(board, i, j+1):
                return True
    board[i][j] = 0
    return False


def valid_board(board, i, j, value):
    is_row_valid = value not in board[i]
    is_col_valid = value not in map(lambda r: r[j], board)
    if not is_row_valid or not is_col_valid:
        return False
    block_y = (i // 3) * 3
    block_x = (j // 3) * 3
    for bi in range(block_y, block_y + 3):
        for bj in range(block_x, block_x + 3):
            if value == board[bi][bj]:
                return False
    return True
