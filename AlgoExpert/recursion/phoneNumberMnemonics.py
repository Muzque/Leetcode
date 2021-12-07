"""


"""
testcases = [
    {
        'input': '1905',
        'output': [
            '1w0j',
            '1w0k',
            '1w0l',
            '1x0j',
            '1x0k',
            '1x0l',
            '1y0j',
            '1y0k',
            '1y0l',
            '1z0j',
            '1z0k',
            '1z0l',
        ],
    },
]

from collections import deque


def phoneNumberMnemonics(phoneNumber):
    cached = {
        '0': ['0'],
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    queue = deque([char for char in phoneNumber])
    arr = ['']
    while queue:
        n = queue.popleft()
        tmp = cached[n]
        arr = [a + t for a in arr for t in tmp]
    return arr


if __name__ == '__main__':
    for tc in testcases:
        ret = phoneNumberMnemonics(tc['input'])
        assert(ret == tc['output'])
