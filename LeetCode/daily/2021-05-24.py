"""
To Lower Case
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3754/
"""
"""
Given a string s, return the string after replacing every uppercase letter 
with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""
testcases = {
    '1': (['Hello'], 'hello'),
    '2': (['here'], 'here'),
    '3': (['LOVELY'], 'lovely'),
    '4': (["al&phaBET"], 'al&phabet')
}

"""
8 / 8 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 14 MB
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(o+32) if 91 > (o := ord(a)) > 64 else a for a in s)
