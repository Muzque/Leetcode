"""

"""
testcases = [
    {
        'input': {
            'words': ["this", "that", "did", "deed", "them!", "a"]
        },
        'output': ["!", "a", "d", "d", "e", "e", "h", "i", "m", "s", "t", "t"],
    },
]

"""
def minimumCharactersForWords(words):
    cached = {}
    for word in words:
        tmp = {}
        for s in word:
            tmp[s] = tmp.get(s, 0) + 1
        for k, v in tmp.items():
            cached[k] = max(cached.get(k, 0), v)
    return [k for k, v in cached.items() for _ in range(v)]
"""


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=minimumCharactersForWords,
        mode='sort',
    )


def minimumCharactersForWords(words):
    ret = []
    cached = {}
    for word in words:
        tmp = {}
        for s in word:
            tmp[s] = tmp.get(s, 0) + 1
        for k, v in tmp.items():
            diff = v - cached.get(k, 0)
            if diff > 0:
                cached[k] = cached.get(k, 0) + diff
                ret += [k] * diff
    return ret
