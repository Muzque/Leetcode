"""

"""
testcases = [
    {
        'input': (4, 2),
        'output': 5,
    },
]


def staircaseTraversal(height, maxSteps):
    ret = 0
    steps = [i for i in range(1, maxSteps+1)]
    queue = [height]
    while queue:
        h = queue.pop()
        for step in steps:
            n = h - step
            if n == 0:
                ret += 1
            elif n > 0:
                queue.append(n)
    return ret


if __name__ == '__main__':
    for tc in testcases:
        ret = staircaseTraversal(*tc['input'])
        assert(ret == tc['output'])
