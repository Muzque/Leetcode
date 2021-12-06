"""

ret = 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)

"""
testcases = [
    {
        'input': [5, 2, [7, -1], 3, [6, [-13, 8], 4]],
        'output': 12,
    },
    {
        'input': [1, 2, [3], 4, 5],
        'output': 18,
    },
]

"""
def productSum(array):
    def rec(obj, layer):
        if isinstance(obj, int):
            return obj
        n = 0
        for ele in obj:
            n += rec(ele, layer+1)
        return n * layer
    ret = 0
    for ele in array:
        ret += rec(ele, layer=2)
    return ret
"""


def productSum(array, layer=1):
    ret = 0
    for ele in array:
        ret += productSum(ele, layer+1) if isinstance(ele, list) else ele
    return ret * layer


if __name__ == '__main__':
    for tc in testcases:
        ret = productSum(tc['input'])
        assert(ret == tc['output'])
