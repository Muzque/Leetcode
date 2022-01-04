"""

"""
testcases = [
    {
        'input': {
            "height": 3,
            "width": 4
        },
        'output': 10,
    },
    {
        'input': {
            "height": 3,
            "width": 2
        },
        'output': 3,
    },
    {
        'input': {
            "height": 1,
            "width": 2
        },
        'output': 1,
    },
    {
        'input': {
            "height": 2,
            "width": 1
        },
        'output': 1,
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=numberOfWaysToTraverseGraph,
    )


def numberOfWaysToTraverseGraph(width, height):
    dp = [[1 for _ in range(width)] for _ in range(height)]
    for i in range(1, height):
        for j in range(1, width):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
