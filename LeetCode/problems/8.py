"""
8. String to Integer (atoi)
Medium

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or '+'.
        Read this character in if it is either.
        This determines if the final result is negative or positive respectively.
        Assume the result is positive if neither is present.
    3 Read in next the characters until the next non-digit character or the end of the input is reached.
        The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
        If no digits were read, then the integer is 0.
        Change the sign as necessary (from step 2).
    5 If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
        then clamp the integer so that it remains in the range.
        Specifically, integers less than -231 should be clamped to -231,
        and integers greater than 231 - 1 should be clamped to 231 - 1.
    6. Return the integer as the final result.

Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""
testcases = [
    {
        'input': {
            's': '42'
        },
        'output': 42
    },
    {
        'input': {
            's': '        -42'
        },
        'output': -42
    },
    {
        'input': {
            's': '4193 with words'
        },
        'output': 4194
    },
    {
        'input': {
            's': '+4.2'
        },
        'output': 4
    },
    {
        'input': {
            's': '.42'
        },
        'output': 0
    },
    {
        'input': {
            's': '+'
        },
        'output': 0
    },
    {
        'input': {
            's': '4212313123214231232'
        },
        'output': 2147483647
    },
    {
        'input': {
            's': '-4212313123214231232'
        },
        'output': -2147483648
    },
]


# 32ms 86.58% | 14.3MB 24.99%
class Solution:
    def get_state(self, w):
        if w == ' ':
            return 0
        if w in ['+', '-']:
            return 1
        if w.isnumeric():
            return 2
        return 3

    def myAtoi(self, s: str) -> int:
        char = ''
        state = 0
        fsm = [
            [0, 1, 2, -1],
            [-1, -1, 2, -1],
            [-1, -1, 2, -1],
            [-1, -1, -1, -1]
        ]
        for w in s:
            move = self.get_state(w)
            state = fsm[state][move]
            if state == -1:
                break
            if state > 0:
                char += w
        if not char or (len(char) == 1 and char in ['+', '-']):
            return 0
        val = int(char)
        if val > 2147483647:
            return 2147483647
        if val < -2147483648:
            return -2147483648
        return val

