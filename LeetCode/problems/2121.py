"""
2121. Intervals Between Identical Elements
Difficulty:Medium

You are given a 0-indexed array of n integers arr.
The interval between two elements in arr is defined as the absolute difference between their indices.
More formally, the interval between arr[i] and arr[j] is |i - j|.

Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i]
and each element in arr with the same value as arr[i].

Note: |x| is the absolute value of x.
"""
from typing import List
from collections import defaultdict

testcases = [
    {
        'input': {
            'arr': [2, 1, 3, 1, 2, 3, 3]
        },
        'output': [4, 2, 7, 2, 4, 4, 5]
    },
    {
        'input': {
            'arr': [10, 5, 10, 10]
        },
        'output': [5, 0, 3, 4]
    },
]


from lib import run_tests


def main():
    kls = Solution()
    run_tests(
        testcases=testcases,
        function=kls.getDistances,
    )


# TLE
class Solution0:

    def getDistances(self, arr: List[int]) -> List[int]:
        result = []
        cached = defaultdict(list)
        for i, num in enumerate(arr):
            cached[num].append(i)
        for j, n in enumerate(arr):
            value = 0
            for k in cached[n]:
                if k < j:
                    value += j - k
                else:
                    value += k - j
            result.append(value)
        return result


# 1520ms, PR25
class Solution1:

    def getDistances(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)
        presum, sufsum = {}, {}
        cnt = {}
        for i in range(len(arr)):
            presum[arr[i]] = presum.get(arr[i], 0) + i
            cnt[arr[i]] = cnt.get(arr[i], 0) + 1
            result[i] += cnt[arr[i]] * i - presum[arr[i]]
        cnt = {}
        for i in range(len(arr)-1, -1, -1):
            sufsum[arr[i]] = sufsum.get(arr[i], 0) + i
            cnt[arr[i]] = cnt.get(arr[i], 0) + 1
            result[i] += sufsum[arr[i]] - cnt[arr[i]] * i
        return result


# 1316ms, PR100
class Solution:

    def getDistances(self, arr: List[int]) -> List[int]:
        presum = [0] * len(arr)
        sufsum = [0] * len(arr)
        cached = defaultdict(list)
        for i, num in enumerate(arr):
            cached[num].append(i)

        for n, subarr in cached.items():
            for i in range(1, len(subarr)):
                presum[subarr[i]] = presum[subarr[i-1]] + i * (subarr[i] - subarr[i-1])
            for i in range(len(subarr)-2, -1, -1):
                sufsum[subarr[i]] = sufsum[subarr[i+1]] + (len(subarr) - 1 - i) * (subarr[i+1] - subarr[i])

        result = [presum[i]+sufsum[i] for i in range(len(arr))]
        return result

      
if __name__ == '__main__':
    tc = testcases[0]
    kls = Solution()
    ret = kls.getDistances(**tc['input'])
