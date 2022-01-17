"""
290. Word Pattern
Easy

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        array = s.split(' ')
        if len(array) != len(pattern):
            return False
        cached = {}
        for i, word in enumerate(array):
            pat = pattern[i]
            if pat not in cached:
                cached[pat] = word
            elif cached[pat] != word:
                return False
        return len(cached) == len(set(cached.values()))
