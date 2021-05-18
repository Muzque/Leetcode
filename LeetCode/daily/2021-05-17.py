"""
Longest String Chain
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3746/
"""
"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one
letter anywhere in word1 to make it equal to word2. For example, "abc" is a
predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3,
and so on.

Return the longest possible length of a word chain with words chosen from the
given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""

testcases = {
    '1': ([["a", "b", "ba", "bca", "abcde", "bda", "bdca"]], 4),
    '2': ([["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]], 5),
    '3': ([['a', 'a', 'a', 'ab']], 2),
    '4': ([['a', 'abc']], 1),
    '5': ([['ab', 'abc', 'abcde', 'abcdef', 'abcdefg']], 3),
}


from typing import List


"""
78 / 78 test cases passed.
Status: Accepted
Runtime: 128 ms
Memory Usage: 14.7 MB
"""


# Avg: 0.06
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        dp = [1] * len(words)
        cache = {}
        for idx, word in enumerate(words):
            for i in range(len(word)):
                w = word[:i]+word[i+1:]
                if w in cache:
                    dp[idx] = max(dp[idx], dp[cache[w]]+1)
            cache[word] = idx
        return max(dp)
