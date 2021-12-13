"""

"""
testcases = [
    {
        'input': {
            'string': 'abaxyzzyxf'
        },
        'output': 'xyzzyx',
    },
    {
        'input': {
            'string': 'a'
        },
        'output': 'a'
    },
]

"""
# TLE
from collections import deque


def isPalindromic(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def get_possibility(string):
    queue = deque(string)
    arr = []
    while queue:
        w = queue.popleft()
        arr += [s + w for s in arr] + [w]
    return sorted(arr, key=len, reverse=True)


def longestPalindromicSubstring(string):
    longest = 0
    ret = ''
    array = get_possibility(string)
    for word in array:
        if len(word) > longest and isPalindromic(word):
            longest = len(word)
            ret = word
    return ret
"""


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=longestPalindromicSubstring,
    )


def isPalindromic(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def longestPalindromicSubstring(string):
    ret = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if len(substring) > len(ret) and isPalindromic(substring):
                ret = substring
    return ret
