testcases = [
    {
        'input': {
            "denoms": [1, 5, 10],
            "n": 7
        },
        'output': 3
    },
    {
        'input': {
            "denoms": [1, 2, 3],
            "n": 0
        },
        'output': 0,
    },
    {
        'input': {
            "denoms": [3, 5],
            "n": 9
        },
        'output': 3
    }
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=minNumberOfCoinsForChange,
    )


def minNumberOfCoinsForChange(n, denoms):
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for denom in denoms:
        for i in range(denom, n+1):
            dp[i] = min(dp[i], dp[i-denom]+1)
    return dp[n] if dp[n] != float('inf') else -1
