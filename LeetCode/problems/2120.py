"""
2120. Execution of All Suffix Instructions Staying in a Grid
Difficulty:Medium

There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1).
You are given the integer n and an integer array startPos where startPos = [startrow, startcol]
indicates that a robot is initially at cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith instruction
for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).

The robot can begin executing from any ith instruction in s. It executes the instructions one by one
towards the end of s but it stops if either of these conditions is met:

The next instruction will move the robot off the grid.
There are no more instructions left to execute.
Return an array answer of length m where answer[i] is the number of instructions the robot can execute
if the robot begins executing from the ith instruction in s.
"""
testcases = [
    {
        'input': {
            'n': 3,
            'startPos': [0, 1],
            's': 'RRDDLU'
        },
        'output': [1, 5, 4, 3, 1, 0]
    }
]

from typing import List


class Solution:
    def get_directions(self, s):
        cached = {
            'U': (0, -1),
            'L': (-1, 0),
            'R': (1, 0),
            'D': (0, 1)
        }
        directions = []
        for w in s:
            directions.append(cached[w])
        return directions

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        directions = self.get_directions(s)
        for i in range(len(directions)):
            step = 0
            y, x = startPos
            for dx, dy in directions[i:]:
                y += dy
                x += dx
                if x >= n or y >= n or x < 0 or y < 0:
                    result.append(step)
                    break
                step += 1
            else:
                result.append(step)
        return result
