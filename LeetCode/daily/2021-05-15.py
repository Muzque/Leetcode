"""
Valid Number
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3744/
"""
"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: 
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", 
"53.5e93", "-123.456e789"], 
while the following are not valid numbers: 
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), 
digits (0-9), plus '+', minus '-', or dot '.'.
"""

testcases = {
    '1': (['0'], True),
    '2': (['e'], False),
    '3': (['.'], False),
    '4': (['.1'], True),
    '5': (['3e+7'], True),
    '6': (['+6e-1'], True),
    '7': (['95a54e53'], False),
    '8': (['99e2.5'], False),
    '9': (['--6'], False),
    '10': (['e3'], False),
    '11': (['-+3'], False),
    '12': (['0e'], False),
    '13': (['3.'], True),
    '14': (['.e1'], False),
    '15': (['6+7'], False),
    '16': (['+.'], False),
    '17': (['46.e3'], True),
    '18': (['4e+'], False),
}


"""
1488 / 1488 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 14.4 MB
"""
"""
https://leetcode.com/problems/valid-number/discuss/23725/C%2B%2B-My-thought-with-DFA
Deterministic Finite Automata method(DFA)
"""


# Avg: 0.0
class Solution:
    def _get_type(self, w: str):
        if w.isnumeric():
            return 0
        if w == '.':
            return 1
        if w == 'e' or w == 'E':
            return 2
        if w == '+' or w == '-':
            return 3
        return 4

    def isNumber(self, s: str) -> bool:
        dfa = [
            [2, 8, -1, 1, -1],
            [2, 8, -1, -1, -1],
            [2, 3, 5, -1, -1],
            [4, -1, 5, -1, -1],
            [4, -1, 5, -1, -1],
            [7, -1, -1, 6, -1],
            [7, -1, -1, -1, -1],
            [7, -1, -1, -1, -1],
            [4, -1, -1, -1, -1],
        ]
        state = 0
        valid_states = '101110010'
        for w in s:
            t = self._get_type(w)
            state = dfa[state][t]
            if state == -1:
                return False
        return valid_states[state] == '1'
