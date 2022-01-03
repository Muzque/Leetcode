"""
997. Find the Town Judge

In a town, there are n people labeled from 1 to n.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that
the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified,
or return -1 otherwise.
"""
testcases = [
    {
        'input': {
            'n': 2,
            'trust': [[1, 2]]
        },
        'output': 2
    },
    {
        'input': {
            'n': 3,
            'trust': [[1, 3], [2, 3]]
        },
        'output': 3
    },
    {
        'input': {
            'n': 3,
            'trust': [[1, 3], [2, 3], [3, 1]]
        },
        'output': -1
    },
    {
        'input': {
            'n': 4,
            'trust': [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
        },
        'output': 3
    },
    {
        'input': {
            'n': 1,
            'trust': [],
        },
        'output': 1,
    }
]

from typing import List
from lib import run_tests


def main():
    kls = Solution()
    run_tests(
        testcases=testcases,
        function=kls.findJudge,
    )


# 966ms 13.31% | 18.9MB 87.18%
class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        chosen = None
        candidate = {}
        for arr in trust:
            civilian, judge = arr
            candidate[civilian] = -1
            if candidate.get(judge, 0) != -1:
                candidate[judge] = candidate.get(judge, 0) + 1
            if chosen is None or candidate[judge] > candidate[chosen]:
                chosen = judge
        count = candidate.get(chosen, -1)
        return chosen if count == n-1 else -1


# 744ms 50.36% | 19MB 23.32%
class Solution2:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        chosen = 1
        candidate = dict((i, 0) for i in range(1, n+1))
        for civilian, judge in trust:
            candidate[civilian] = -1
            if candidate[judge] != -1:
                candidate[judge] += 1
            if candidate[judge] > candidate[chosen]:
                chosen = judge
        return chosen if candidate[chosen] == n-1 else -1


# 744ms 50.36% | 18.8MB 87.18%
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cached = [0] * (n + 1)
        for i, j in trust:
            cached[i] -= 1
            cached[j] += 1
        for i in range(1, n+1):
            if cached[i] == n-1:
                return i
        return -1
