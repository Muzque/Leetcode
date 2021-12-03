"""

"""
testcases = [
    {
        'input': ("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"),
        'output': True,
    },
]


def count(string):
    cached = {}
    for s in string:
        cached[s] = cached.get(s, 0) + 1
    return cached


def generateDocument(characters, document):
    cached_c = count(characters)
    cached_d = count(document)
    for k, v in cached_d.items():
        r = cached_c.pop(k, 0)
        if r < v:
            return False
    return True


if __name__ == '__main__':
    for tc in testcases:
        ret = generateDocument(*tc['input'])
        assert(ret == tc['output'])
