"""
Ambiguous Coordinates
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3741/
"""

testcases = {
    '1': (["(123)"], ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]),
    '2': (["(00011)"], ["(0.001, 1)", "(0, 0.011)"]),
    '3': (["(0123)"], ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]),
    '4': (["(100)"], ["(10, 0)"]),
}


from typing import List


"""
346 / 346 test cases passed.
Status: Accepted
Runtime: 48 ms
Memory Usage: 14.2 MB
"""


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        arr = []
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            left_arr = self._get_possibility(left)
            right_arr = self._get_possibility(right)
            for la in left_arr:
                for ra in right_arr:
                    arr.append(f'({la}, {ra})')
        return arr

    def _get_possibility(self, word):
        arr = []
        if len(word) == 1 or word[0] != '0':
            arr.append(word)
        for i in range(1, len(word)):
            w = f'{word[:i]}.{word[i:]}'
            if w[-1] == '0' or (i > 1 and w[0] == '0'):
                continue
            arr.append(w)
        return arr
