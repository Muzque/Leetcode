testcases = [
    {
        'input': {
            "string": "clementisacap"
        },
        'output': 'mentisac',
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=longestSubstringWithoutDuplication,
    )


def longestSubstringWithoutDuplication(string):
    cached = {}
    ret = ''
    pt = 0
    for i, s in enumerate(string):
        if s in cached:
            if cached[s] < pt:
                cached[s] = i
            else:
                pt = max(cached[s] + 1, pt + 1)
        cached[s] = i
        if (i - pt + 1) > len(ret):
            ret = string[pt:i + 1]
    return ret
