"""

"""

testcases = [
    {
        'input': {
            'string': 'abcdcba'
        },
        'output': True
    },
    {
        'input': {
            'string': 'abba'
        },
        'output': True,
    },
    {
        'input': {
            'string': 'abca'
        },
        'output': False,
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=isPalindrome,
    )


def isPalindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
