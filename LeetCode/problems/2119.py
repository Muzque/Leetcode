"""
2119. A Number After a Double Reversal
Difficulty:Easy

Reversing an integer means to reverse all its digits.
 * For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.

Given an integer num, reverse num to get reversed1, then reverse reversed1
to get reversed2. Return true if reversed2 equals num. Otherwise return false.


Constraints:
 * 0 <= num <= 106
"""

testcases = [
    {
        'input': {
            'num': 256,
        },
        'output': True,
    },
    {
        'input': {
            'num': 1800,
        },
        'output': False,
    },
    {
        'input': {
            'num': 0,
        },
        'output': True,
    },
]


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return num % 10 != 0
