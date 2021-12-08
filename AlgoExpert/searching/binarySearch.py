"""

"""
testcases = [
    {
        'input': (
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
            33
        ),
        'output': 3,
    },
    {
        'input': (
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
            34
        ),
        'output': -1,
    },
    {
        'input': (
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
            45
        ),
        'output': 4,
    },
    {
        'input': (
            [1, 5, 23, 111],
            111
        ),
        'output': 3,
    },
    {
        'input': (
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
            0
        ),
        'output': 0,
    },
]


def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        pt = (left + right) // 2
        if array[pt] == target:
            return pt
        if array[pt] > target:
            right = pt - 1
        else:
            left = pt + 1
    return -1


if __name__ == '__main__':

    for idx, tc in enumerate(testcases):
        print(f'Question {idx+1}:')
        ret = binarySearch(*tc['input'])
        print(f'Ans: {ret}')
        assert(ret == tc['output'])
