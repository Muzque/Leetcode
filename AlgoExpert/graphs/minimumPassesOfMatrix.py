"""

"""
from copy import deepcopy

testcases = [
    {
        'input': [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1]
        ],
        'output': 3,
    },
    {
        'input': [
            [1, 2, 3],
            [4, 5, 6]
        ],
        'output': 0,
    },
]


def has_positive_neighbor(matrix, i, j):
    h = len(matrix)
    w = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d in directions:
        y, x = i + d[0], j + d[1]
        if h > y >= 0 and w > x >= 0 and matrix[y][x] > 0:
            return True
    return False


def minimumPassesOfMatrix(matrix, count=0):
    cached = deepcopy(matrix)
    is_updated = False
    is_end = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                if has_positive_neighbor(cached, i, j):
                    matrix[i][j] *= -1
                    is_updated = True
                else:
                    is_end = False
    if is_end:
        return count + 1 if is_updated else count
    if cached == matrix:
        return -1
    return minimumPassesOfMatrix(matrix, count + 1)


if __name__ == '__main__':
    for tc in testcases:
        ret = minimumPassesOfMatrix(tc['input'])
        try:
            assert(ret == tc['output'])
        except Exception as e:
            print(f'Input: {tc["input"]}')
            print(f'Yours: {ret}')
            print(f'Ans: {tc["output"]}')
            raise e

