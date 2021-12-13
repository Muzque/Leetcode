"""

"""
from collections import defaultdict

testcases = [
    {
        'input': {
            'string': 'abcceedfdfa'
        },
        'output': 1,
    },
    {
        'input': {
            'string': 'abbcac'
        },
        'output': -1,
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=firstNonRepeatingCharacter,
    )


def firstNonRepeatingCharacter(string):
    cached = defaultdict(list)
    for idx, s in enumerate(string):
        cached[s].append(idx)
    for v in cached.values():
        if len(v) == 1:
            return v[0]
    return -1
