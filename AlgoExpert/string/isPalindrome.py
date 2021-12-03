"""

"""

testcases = [
    {
        'input': 'abcdcba',
        'output': True
    },
    {
        'input': 'abba',
        'output': True,
    },
    {
        'input': 'abca',
        'output': False,
    },
]


def isPalindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True


if __name__ == '__main__':
    for tc in testcases:
        ret = isPalindrome(tc['input'])
        assert(ret == tc['output'])
