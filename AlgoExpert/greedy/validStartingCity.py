"""

"""
testcases = [
    # {
    #     'input': (
    #         [5, 25, 15, 10, 15],
    #         [1, 2, 1, 0, 3],
    #         10
    #     ),
    #     'output': 4,
    # },
    {
        'input': (
            [30, 40, 10, 10, 17, 13, 50, 30, 10, 40],
            [1, 2, 0, 1, 1, 0, 3, 1, 0, 1],
            25
        ),
        'output': 1,
    },
]


def validStartingCity(distances, fuel, mpg):
    h = len(distances)
    for i in range(h):
        tank = 0
        for j in range(h):
            z = i + j if i + j < h else i + j - h
            tank += fuel[z] * mpg - distances[z]
            if tank < 0:
                break
        else:
            return i
    return -1


if __name__ == '__main__':
    for tc in testcases:
        ret = validStartingCity(*tc['input'])
        assert(ret == tc['output'])
