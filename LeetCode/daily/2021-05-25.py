"""
Evaluate Reverse Polish Notation
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3755/
"""
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another 
expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the 
expression would always evaluate to a result, and there will not be any 
division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the 
range [-200, 200].
"""
testcases = {
    '1': ([["2", "1", "+", "3", "*"]], 9),
    '2': ([["4", "13", "5", "/", "+"]], 6),
    '3': ([["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]], 22),
}

from typing import List
import operator

"""
20 / 20 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 14.6 MB
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        arr = []
        for token in tokens:
            if token in ops:
                op = ops[token]
                b = arr.pop()
                a = arr.pop()
                arr.append(int(op(a, b)))
            else:
                arr.append(int(token))
        return arr[-1]
