"""

"""
testcases = [
    {
        'input': (
            3,
            [1, 3, 5, 3, 1, 4],
        ),
        'output': [
          [4, 2],
          [0, 5],
          [3, 1]
        ],
    },
]


def taskAssignment(k, tasks):
    arr = sorted(range(len(tasks)), key=lambda x: tasks[x])
    ret = []
    for i in range(len(arr) // 2):
        ret.append([arr[i], arr[len(arr)-i-1]])
    return ret


if __name__ == '__main__':
    for tc in testcases:
        ret = taskAssignment(*tc['input'])
        assert(ret == tc['output'])
