"""
1345. Jump Game IV
Hard

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
"""
testcases = [
    {
        'input': {
            'arr': [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
        },
        'output': 3
    },
    {
        'input': {
            'arr': [7]
        },
        'output': 0
    },
    {
        'input': {
            'arr': [7, 6, 9, 6, 9, 6, 9, 7]
        },
        'output': 1
    },
    {
        'input': {
            'arr': [
                51, 64, -15, 58, 98, 31, 48, 72, 78, -63, 92,
                -5, 64, -64, 51, -48, 64, 48, -76, -86, -5, -64,
                -86, -47, 92, -41, 58, 72, 31, 78, -15, -76, 72,
                -5, -97, 98, 78, -97, -41, -47, -86, -97, 78, -97,
                58, -41, 72, -41, 72, 25, -76, 51, -86, -65, 8,
                -63, 72, -15, 48, -15, -63, -65, 31, 41, 95, 51,
                -47, 51, -41, -76, 58, -81, -41, 88, 58, -81, 88,
                88, -47, -48, 72, -25, -86, -41, -86, -64, -15, -63
            ]
        },
        'output': 4
    },
]

from typing import List


# TLE
class Solution0:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        cached = {}
        for i, num in enumerate(arr):
            if num not in cached:
                cached[num] = [i]
            else:
                cached[num].append(i)
        queue = [(0, 0)]
        while queue:
            size = len(queue)
            tmp = None
            for _ in range(size):
                step, i = queue.pop(0)
                if i == len(arr) -1:
                    return step
                if arr[i] == arr[-1]:
                    tmp = step + 1
                queue.append((step+1, i+1))
                if i > 0:
                    queue.append((step+1, i-1))
                for j in cached[arr[i]]:
                    if j != i:
                        queue.append((step+1, j))
            if tmp is not None:
                return tmp


# TLE
class Solution1:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        cached = {}
        for i, num in enumerate(arr):
            if num not in cached:
                cached[num] = [i]
            else:
                cached[num].append(i)
        queue = [(0, 0)]
        visited = {0}
        while queue:
            size = len(queue)
            tmp = None
            for _ in range(size):
                step, i = queue.pop(0)
                if i == len(arr) - 1:
                    return step
                if arr[i] == arr[-1]:
                    tmp = step + 1
                if i+1 not in visited:
                    visited.add(i+1)
                    queue.append((step+1, i+1))
                if i > 0 and i-1 not in visited:
                    visited.add(i-1)
                    queue.append((step+1, i-1))
                for j in cached[arr[i]]:
                    if j != i and j not in visited:
                        visited.add(j)
                        queue.append((step+1, j))
            if tmp is not None:
                return tmp


from collections import defaultdict


# TLE
class Solution2:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        cached = defaultdict(list)
        for i, num in enumerate(arr[1:-1], 1):
            if num != arr[i+1] or num != arr[i-1]:
                cached[num].append(i)
        cached[num].append(i)
        queue = [(0, 0)]
        visited = {0}
        while queue:
            size = len(queue)
            tmp = None
            for _ in range(size):
                step, i = queue.pop(0)
                if i == len(arr) - 1:
                    return step
                if arr[i] == arr[-1]:
                    tmp = step + 1
                if i+1 not in visited:
                    visited.add(i+1)
                    queue.append((step+1, i+1))
                if i > 0 and i-1 not in visited:
                    visited.add(i-1)
                    queue.append((step+1, i-1))
                for j in cached[arr[i]]:
                    if j != i and j not in visited:
                        visited.add(j)
                        queue.append((step+1, j))
            if tmp is not None:
                return tmp


# 1285ms 10.39% | 28.8MB 68.22%
class Solution3:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        cached = defaultdict(list)
        for i, num in enumerate(arr[1:-1], 1):
            if num != arr[i+1] or num != arr[i-1]:
                cached[num].append(i)
        cached[num].append(i)
        queue = [(0, 0)]
        visited = {0}
        while queue:
            size = len(queue)
            tmp = None
            for _ in range(size):
                step, i = queue.pop(0)
                if i == len(arr) - 1:
                    return step
                if arr[i] == arr[-1]:
                    tmp = step + 1
                if i+1 not in visited:
                    visited.add(i+1)
                    queue.append((step+1, i+1))
                if i > 0 and i-1 not in visited:
                    visited.add(i-1)
                    queue.append((step+1, i-1))
                for j in cached[arr[i]]:
                    if j != i and j not in visited:
                        visited.add(j)
                        queue.append((step+1, j))
                cached[arr[i]] = []
            if tmp is not None:
                return tmp


# 1336ms 9.19% | 29.1MB 57.23%
class Solution4:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        cached = defaultdict(list)
        for i, num in enumerate(arr):
            cached[num].append(i)

        queue = [(0, len(arr) - 1)]
        visited = {len(arr) - 1}
        while queue:
            step, i = queue.pop(0)
            if i + 1 < len(arr) and i + 1 not in visited:
                visited.add(i + 1)
                queue.append((step + 1, i + 1))
            if i - 1 not in visited:
                if i - 1 == 0:
                    return step + 1
                visited.add(i - 1)
                queue.append((step + 1, i - 1))
            for j in cached[arr[i]]:
                if j == 0:
                    return step + 1
                if j != i and j not in visited:
                    visited.add(j)
                    queue.append((step + 1, j))
            cached[arr[i]] = []


# 924ms 25.6% | 27.5MB 89.46%
class Solution5:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        cached = defaultdict(list)
        for i, num in enumerate(arr):
            cached[num].append(i)

        visited = [0] * len(arr)
        queue = [len(arr) - 1]
        while queue:
            i = queue.pop(0)
            if i + 1 < len(arr) - 1 and visited[i + 1] == 0:
                visited[i + 1] = visited[i] + 1
                queue.append(i + 1)
            if visited[i - 1] == 0:
                visited[i - 1] = visited[i] + 1
                if i - 1 == 0: return visited[0]
                queue.append(i - 1)
            for j in cached[arr[i]]:
                if j != i and visited[j] == 0:
                    visited[j] = visited[i] + 1
                    if j == 0: return visited[j]
                    queue.append(j)
            cached[arr[i]] = []


# 584ms 93.22% | 27.5MB 91.11%
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        cached = defaultdict(list)
        for i, num in enumerate(arr):
            cached[num].append(i)

        visited = [0] * len(arr)
        queue = [len(arr) - 1]
        while queue:
            i = queue.pop(0)
            if i + 1 < len(arr) - 1 and visited[i + 1] == 0:
                visited[i + 1] = visited[i] + 1
                queue.append(i + 1)
            if visited[i - 1] == 0:
                visited[i - 1] = visited[i] + 1
                if i - 1 == 0: return visited[0]
                queue.append(i - 1)
            for j in cached[arr[i]]:
                if j != i and visited[j] == 0:
                    visited[j] = visited[i] + 1
                    if j == 0: return visited[j]
                    queue.append(j)
            cached.pop(arr[i])
