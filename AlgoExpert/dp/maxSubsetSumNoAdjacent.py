"""

"""
testcases = [
    {
        'input': {
            "array": [75, 105, 120, 75, 90, 135]
        },
        'output': 330
    }
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=maxSubsetSumNoAdjacent,
    )


def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    if len(array) <= 2:
        return max(array)
    dp = [0] * len(array)
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        dp[i] = max(dp[i-2]+array[i], dp[i-1])
    return dp[-1]
