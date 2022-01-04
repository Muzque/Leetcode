"""

"""
testcases = [
    {
        'input': {
            "str1": "abc",
            "str2": "yabd"
        },
        'output': 2,
    }
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=levenshteinDistance,
    )


def levenshteinDistance(str1, str2):
    dp = [[i+j if i*j == 0 else 0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]
