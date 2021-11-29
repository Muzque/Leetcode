"""
Given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of
that character is a reversal of the part of the string to its right.
The function should return −1 if no such index exists.

For example, given a string:
    "racecar"

the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one
to the right is "car".

Given a string:
    "x"

the function should return 0, because both substrings are empty.

Write an efficient algorithm for the following assumptions:
    - the length of S is within the range [0..2,000,000].
"""
testcases = [
    {
        'input': 'racecar',
        'output': 3,
    },
    {
        'input': 'x',
        'output': 0,
    },
    {
        'input': '',
        'output': -1
    },
    {
        'input': 'abba',
        'output': -1,
    },
]


# Task Score: 100%
# Correctness: 100%
# Performance: 100%
# Time: O(length(S))
def solution(S):
    if len(S) % 2 == 0:
        return -1
    mid = len(S) // 2
    for i in range(mid):
        if S[i] != S[len(S)-i-1]:
            return -1
    return mid


if __name__ == '__main__':
    for tc in testcases:
        ret = solution(tc['input'])
        assert(ret == tc['output'])
