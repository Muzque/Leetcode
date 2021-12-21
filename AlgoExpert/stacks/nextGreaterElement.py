"""

"""
testcases = [
    {
        'input': {
            "array": [2, 5, -3, -4, 6,  ]
        },
        'output': [5, 6, 6, 6, 7, -1, 5],
    },
    {
        'input': {
            "array": [0, 1, 2, 3, 4]
        },
        'output': [1, 2, 3, 4, -1]
    },
    {
        'input': {
            "array": [12, 4]
        },
        'output': [-1, 12]
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=nextGreaterElement,
    )


# 41.4 MiB space
"""
def find_greater_index(array, num):
    for i in range(len(array)):
        if array[i] > num:
            return array[i]
    return -1


def nextGreaterElement(array):
    ret = []
    for i in range(len(array)):
        check = array[i+1:] + array[:i]
        num = find_greater_index(check, array[i])
        ret.append(num)
    return ret
"""


# 41.2 MiB space
"""
def nextGreaterElement(array):
    result = [-1] * len(array)
    for i in range(len(array)):
        counter = 1
        while counter < len(array):
            j = (i + counter) % len(array)
            if array[j] > array[i]:
                result[i] = array[j]
                break
            counter += 1
    return result
"""


# 41.2 MiB space
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []
    for idx in range(2 * len(array)):
        i = idx % len(array)
        while len(stack) > 0 and array[stack[-1]] < array[i]:
            j = stack.pop()
            result[j] = array[i]
        stack.append(i)
    return result
