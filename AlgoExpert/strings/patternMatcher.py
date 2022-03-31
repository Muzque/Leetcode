testcases = [
    {
        'input': {
            "pattern": "xxyxxy",
            "string": "gogopowerrangergogopowerranger"
        },
        'output': ["go", "powerranger"]
    },
    {
        'input': {
            "pattern": "yxyx",
            "string": "abab"
        },
        'output': ['b', 'a'],
    },
    {
        'input': {
            "pattern": "yxx",
            "string": "yomama"
        },
        'output': ['ma', 'yo'],
    },
    {
        'input': {
            "pattern": "xxxx",
            "string": "testtesttesttest"
        },
        'output': ['test', '']
    },
    {
        'input': {
            "pattern": "yxyyyxxy",
            "string": "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"
        },
        'output': ["baddaddoomi", "baddaddoom"],
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=patternMatcher,
    )


# This is for unlimited number of type in pattern such as x, y, z, a, b, c.
# There is only x and y in this question.
"""
def cutter(string, pattern):
    long = 1
    while long < len(string):
        s = string[:long]
        arr = string.replace(s, ' _ ').split()
        if len(arr) > len(pattern):
            long += 1
            continue
        return s
    return ''


def patternMatcher(pattern, string):
    patterns = [p for p in pattern]
    cached = {}
    while string != '':
        s = cutter(string, patterns)
        cached[patterns[0]] = s
        arr = string.replace(s, ' _ ').split()
        string = ''.join([char for char in arr if char != '_'])
        if len(patterns) >= len(arr):
            patterns = [p for p in pattern if p not in cached]
            continue
        return []
    return [v for v in cached.values()]
"""


def get_first_pattern(patterns, string, long, cached):
    s = string[:long]
    arr = string.replace(s, ' _ ').split()
    cached[patterns[0]] = s
    ret = verify_string(string, patterns, cached)
    return cached, arr, ret


def get_second_pattern(patterns, string, array, cached):
    if len(set(patterns)) == 1:
        return []
    second_pattern = next(p for p in patterns if p != patterns[0])
    second_string = next(s for s in array if s != '_')
    if len(array) == len(patterns):
        cached[second_pattern] = second_string
        return verify_string(string, patterns, cached)
    long = 1
    while long <= len(second_string):
        cached[second_pattern] = second_string[:long]
        if cached['y'] == 'baddaddoom':
            print(long, cached, second_string, array)
        ret = verify_string(string, patterns, cached)
        if not ret:
            long += 1
            continue
        return ret
    return []


def verify_string(string, patterns, cached):
    ordering = ['x', 'y']
    tmp = ''.join([cached[p] for p in patterns if p in cached])
    if tmp == string:
        return [cached[p] for p in ordering if p in cached]
    return []


def patternMatcher(pattern, string):
    patterns = [p for p in pattern]
    cached = {'x': '', 'y': ''}
    long = 1
    while long < len(string):
        cached, arr, ret = get_first_pattern(patterns, string, long, cached)
        if ret:
            return ret
        ret = get_second_pattern(patterns, string, arr, cached)
        if ret:
            return ret
        long += 1
    return []
