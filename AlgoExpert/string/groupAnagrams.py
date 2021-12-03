"""

"""
testcases = [
    {
        'input': ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"],
        'output': [
            ["foo"],
            ["flop", "olfp"],
            ["oy", "yo"],
            ["act", "cat", "tac"]
        ],
    },
]


from collections import defaultdict


def groupAnagrams(words):
    cached = defaultdict(list)
    for word in words:
        sword = ''.join(sorted(word))
        cached[sword].append(word)
    return [arr for arr in cached.values()]


if __name__ == '__main__':
    for tc in testcases:
        ret = groupAnagrams(tc['input'])
        assert(ret == tc['output'])
