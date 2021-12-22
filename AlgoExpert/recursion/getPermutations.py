"""

"""
testcases = [
    {
        'input': {
            'array': [1, 2, 3]
        },
        'output': [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ],
    },
    {
        'input': {
            'array': [],
        },
        'output': [],
    },
]

from lib import run_tests


def dfs(array, tmp, result):
    if len(array) == 0:
        result.append(tmp)
        return
    for i in range(len(array)):
        dfs(array[:i] + array[i+1:], tmp + [array[i]], result)
    return


def getPermutations(array):
    if not array:
        return []
    result = []
    dfs(array, [], result)
    return result


def main():
    run_tests(
        testcases=testcases,
        function=getPermutations,
    )
