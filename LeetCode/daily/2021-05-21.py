"""
Find and Replace Pattern
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3750/
"""
"""
Given a list of strings words and a string pattern, return a list of words[i] 
that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that 
after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: 
every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a 
permutation, since a and b map to the same letter.

Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
 

Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""
testcases = {
    '1': ([["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"], ["mee", "aqq"]),
    '2': ([["a", "b", "c"], "a"], ["a", "b", "c"]),
}

from typing import List


"""
46 / 46 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 14.4 MB
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        h = len(pattern)
        result = []
        for word in words:
            cache = {}
            visited = set()
            for i in range(h):
                match = cache.get(pattern[i])
                if match is not None and match != word[i]:
                    break
                visited.add(word[i])
                cache[pattern[i]] = word[i]
            else:
                if len(visited) == len(cache):
                    result.append(word)
        return result
