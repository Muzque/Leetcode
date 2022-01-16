"""
849. Maximize Distance to Closest Person
Medium

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat,
and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.
"""
testcases = [
    {
        'input': {
            'seats': [1, 0, 0, 0, 1, 0, 1],
        },
        'output': 2
    },
    {
        'input': {
            'seats': [1, 0, 0, 0, 0],
        },
        'output': 4
    },
    {
        'input': {
            'seats': [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        },
        'output': 3
    },
]

from typing import List


# 178ms 31.1% | 14.7MB 76.9%
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        tmp = 0
        left = False
        for i, seat in enumerate(seats):
            if seat == 1:
                if left is False:
                    max_dist = tmp
                else:
                    max_dist = max(max_dist, (tmp + 1) // 2)
                left = True
                tmp = 0
            else:
                tmp += 1
        return max(max_dist, tmp)

