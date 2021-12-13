"""

"""
testcases = [
    {
        'input': {
            'words': ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        },
        'output': [
            ["foo"],
            ["flop", "olfp"],
            ["oy", "yo"],
            ["act", "cat", "tac"]
        ],
    },
]


from collections import defaultdict
from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=groupAnagrams,
        mode='sort1',
    )


def groupAnagrams(words):
    cached = defaultdict(list)
    for word in words:
        sword = ''.join(sorted(word))
        cached[sword].append(word)
    return [arr for arr in cached.values()]
