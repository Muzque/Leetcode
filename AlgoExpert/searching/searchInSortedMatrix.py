testcases = [
    {
        'input': {
            "matrix": [
                [1, 4, 7, 12, 15, 1000],
                [2, 5, 19, 31, 32, 1001],
                [3, 8, 24, 33, 35, 1002],
                [40, 41, 42, 44, 45, 1003],
                [99, 100, 103, 106, 128, 1004]
            ],
            "target": 44
        },
        'output': [3, 3]
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=searchInSortedMatrix,
    )


def searchInSortedMatrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            num = matrix[i][j]
            if num == target:
                return [i, j]
            if num > target:
                break
    return [-1, -1]
