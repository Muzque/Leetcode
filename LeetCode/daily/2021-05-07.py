"""
Delete Operation for Two Strings
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3734/
"""
"""
1306 / 1306 test cases passed.
Status: Accepted
Runtime: 272 ms
Memory Usage: 16.2 MB
"""
testcases = {
    '1': (["sea", "eat"], 2),
    '2': (["leetcode", "etco"], 4),
    '3': (["seceea", "beat"], 6),
    '4': (['s', 'se'], 1),
    '5': (['ab', 'cd'], 4),
    '6': (['food', 'money'], 7),
}


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h1 = len(word1)
        h2 = len(word2)
        dp = [[0] * (h1 + 1) for _ in range(h2 + 1)]
        for j in range(1, h2 + 1):
            for i in range(1, h1 + 1):
                if word1[i - 1] == word2[j - 1]:
                   dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
        maxSame = dp[h2][h1]
        return abs(h1 - maxSame) + abs(h2 - maxSame)


if __name__ == '__main__':
    sol = Solution()
    for idx, testcase in testcases.items():
        inputs, ans = testcase
        ret = sol.minDistance(*inputs)
        print(f'Question {idx}:')
        if ret != ans:
            print(
                f'*WrongAnswer index {idx}\n'
                f'answer: {ans}\n'
                f'yours: {ret}\n'
            )
            break
        print('PASS\n')
    else:
        print('Accepted')
