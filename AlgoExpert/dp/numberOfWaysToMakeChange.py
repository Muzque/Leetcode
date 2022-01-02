testcases = [
    {
        'input': {
            "denoms": [1, 5],
            "n": 6
        },
        'output': 2,
    },
    {
        'input': {
            'denoms': [5],
            'n': 10,
        },
        'output': 1
    }
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=numberOfWaysToMakeChange,
    )


def numberOfWaysToMakeChange(n, denoms):
    dp = [0] * (n + 1)
    dp[0] = 1
    for denom in denoms:
        for amount in range(denom, n + 1):
            dp[amount] += dp[amount - denom]
    return dp[n]
