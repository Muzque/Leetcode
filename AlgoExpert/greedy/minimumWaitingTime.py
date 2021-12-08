"""

"""
testcases = [
    {
        'input': [3, 2, 1, 2, 6],
        'output': 17,
    },
    {
        'input': [2],
        'output': 0,
    },
]


def minimumWaitingTime(queries):
    queries.sort()
    queries.pop()
    ret = 0
    for i in range(len(queries)):
        if i > 0:
            queries[i] += queries[i-1]
        ret += queries[i]
    return ret


if __name__ == '__main__':
    for tc in testcases:
        ret = minimumWaitingTime(tc['input'])
        assert(ret == tc['output'])
