"""

"""

testcases = [
    {
        'input': {
            'string': '1921680'
        },
        'output': [
            "1.9.216.80",
            "1.92.16.80",
            "1.92.168.0",
            "19.2.16.80",
            "19.2.168.0",
            "19.21.6.80",
            "19.21.68.0",
            "19.216.8.0",
            "192.1.6.80",
            "192.1.68.0",
            "192.16.8.0"
        ],
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=validIPAddresses,
        mode='sort',
    )


def find_all():
    queue = [1, 2, 3]
    arr = [[1], [2], [3]]
    for _ in range(2):
        arr = [sarr + [sarr[-1] + i] for sarr in arr for i in queue]
    return arr


def validRule(s):
    if s[0] == '0' and len(s) > 1:
        return False
    if int(s) > 255:
        return False
    return True


def validIPAddresses(string):
    ret = []
    pos = find_all()
    for arr in pos:
        if arr[-1] < len(string):
            sarr = [string[:arr[0]]] + [string[arr[i]:arr[i+1]] for i in range(2)] + [string[arr[-1]:]]
            if all(validRule(n) for n in sarr):
                ret.append('.'.join(sarr))
    return ret
