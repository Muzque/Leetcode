"""
Construct Target Array With Multiple Sums
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3737/
"""
"""
68 / 68 test cases passed.
Status: Accepted
Runtime: 256 ms
Memory Usage: 20 MB
"""
testcases = {
    '1': ([[9, 3, 5]], True),
    '2': ([[1, 1, 1, 2]], False),
    '3': ([[8, 5]], True),
    '4': ([[1, 4, 1, 1]], True),
    '5': ([[1, 1, 1]], True),
    '6': ([[1, 3, 5]], True),
    '7': ([[6]], False),
    '8': ([[5, 2]], True),
    '9': ([[1, 1, 4, 1]], True),
    '10': ([[1, 1000000000]], True),
    '11': ([[1, 1, 2]], False),
}

from typing import List


class Solution:

    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]
        init = [1] * len(target)
        while True:
            if target == init:
                return True
            mt = max(target)
            target.remove(mt)
            left = sum(target)
            if left == 1:
                return True
            dt = mt % left
            if dt == mt or dt < 1:
                return False
            target.append(dt)
