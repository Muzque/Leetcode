"""

"""

from collections import deque


testcases = [
    {
        'input': [1, 2],
        'output': [
            [],
            [1],
            [2],
            [1, 2],
        ],
    },
    {
        'input': [1, 2, 3],
        'output': [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3]
        ],
    },
]


def powerset(array):
    queue = deque(array)
    arr = [[]]
    while queue:
        n = queue.popleft()
        arr += [subarr + [n] for subarr in arr]
    return arr


if __name__ == '__main__':
    for tc in testcases:
        ret = powerset(tc['input'])
        assert(ret == tc['output'])
