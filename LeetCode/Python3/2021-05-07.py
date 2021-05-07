testcases = {
    '1': (["sea", "eat"], 2),
    '2': (["leetcode", "etco"], 4),
    '3': (["seceea", "beat"], 6),
    '4': (['s', 'se'], 1),
    '5': (['ab', 'cd'], 4),
}


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h1 = len(word1)
        h2 = len(word2)
        dp = [[0]*(h1+1) for _ in range(h2+1)]
        for i in range(1, h1+1):
            for j in range(1, h2+1):
                currentMax = max(dp[i-1][j], dp[i][j-1])
                if word1[i-1] == word2[j-1]:
                    currentMax += 1
                dp[i][j] = currentMax
        maxSame = dp[h1][h2]
        return abs(h1 - maxSame) + abs(h2 - maxSame)


if __name__ == '__main__':
    sol = Solution()
    for idx, testcase in testcases.items():
        inputs, ans = testcase
        ret = sol.minDistance(*inputs)
        print(f'Question {idx}:\n')
        if ret != ans:
            print(
                f'*WrongAnswer index {idx}\n'
                f'answer: {ans}\n'
                f'yours: {ret}\n'
            )
            break
        print('PASS')
    else:
        print('Accepted')
