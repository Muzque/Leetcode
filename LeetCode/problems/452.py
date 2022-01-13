"""
452. Minimum Number of Arrows to Burst Balloons
Medium

There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon
whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
There is no limit to the number of arrows that can be shot.
A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""
testcases = [
    {
        'input': {
            'points': [
                [3, 9],
                [7, 12],
                [3, 8],
                [6, 8],
                [9, 10],
                [2, 9],
                [0, 9],
                [3, 9],
                [0, 6],
                [2, 8]
            ],
        },
        'output': 2
    }
]

from typing import List
from lib import run_tests


def main():
    kls = Solution()
    run_tests(
        testcases=testcases,
        function=kls.findMinArrowShots,
    )


# TLE
class Solution1:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cached = [points.pop(0)]
        for point in points:
            for array in cached:
                if array[1] >= point[0] >= array[0] or array[1] >= point[1] >= array[0]:
                    array[0] = max(point[0], array[0])
                    array[1] = min(point[1], array[1])
                    break
            else:
                cached.append(point)
        return len(cached)


# 3253ms 5.02% | 59.2MB 35.36%
class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cached = [points.pop(0)]
        for point in points:
            left, right = 0, len(cached)-1
            while left <= right:
                mid = (left + right) // 2
                array = cached[mid]
                if point[0] > array[1]:
                    left = mid + 1
                    continue
                if point[1] < array[0]:
                    right = mid - 1
                    continue
                if array[1] >= point[0] >= array[0] or array[1] >= point[1] >= array[0]:
                    array[0] = max(point[0], array[0])
                    array[1] = min(point[1], array[1])
                    break
            else:
                cached.append(point)
        return len(cached)


# 1264ms 78.54% | 59.2MB 10.57%
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[1])

        cnt = 1
        last_arrow = points[0][1]
        for i in range(1, len(points)):
            if points[i][1] >= last_arrow >= points[i][0]:
                continue
            else:
                cnt += 1
                last_arrow = points[i][1]
        return cnt
