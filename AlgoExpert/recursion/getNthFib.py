"""

"""
testcases = [
    {
        'input': 2,
        'output': 1,
    },
    {
        'input': 6,
        'output': 5,
    },
    {
        'input': 1,
        'output': 0,
    },
]


def getNthFib(n):
    if n < 3:
        return n - 1
    dp = [0, 1] + [1] * (n-2)
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


if __name__ == '__main__':
    for tc in testcases:
        ret = getNthFib(tc['input'])
        assert(ret == tc['output'])
