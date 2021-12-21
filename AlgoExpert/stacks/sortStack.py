"""
Inplace sorting the input array.
"""
testcases = [
    {
        'input': {
            "stack": [-5, 2, -2, 4, 3, 1]
        },
        'output': [-5, -2, 1, 2, 3, 4],
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=sortStack,
    )


def rec(stack, num):
    if len(stack) == 0 or num >= stack[-1]:
        stack.append(num)
        return
    tmp = stack.pop()
    rec(stack, num)
    stack.append(tmp)


# O(n^2) time | O(n) space - where n is the length of the stack
def sortStack(stack):
    if len(stack) == 0:
        return stack
    num = stack.pop()
    sortStack(stack)
    rec(stack, num)
    return stack
