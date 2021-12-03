"""

"""
from collections import defaultdict

testcases = [
    {
        'input': 'abcceedfdfa',
        'output': 1,
    },
    {
        'input': 'abbcac',
        'output': -1,
    },
]


def firstNonRepeatingCharacter(string):
    cached = defaultdict(list)
    for idx, s in enumerate(string):
        cached[s].append(idx)
    for v in cached.values():
        if len(v) == 1:
            return v[0]
    return -1


if __name__ == '__main__':
    for tc in testcases:
        ret = firstNonRepeatingCharacter(tc['input'])
        assert(ret == tc['output'])
