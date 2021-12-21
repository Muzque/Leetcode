"""

"""
testcases = [
    {
        'input': {
            "array": [2, 5, -3, -4, 6, 7, 2]
        },
        'output': [5, 6, 6, 6, 7, -1, 5],
    }
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=nextGreaterElement,
    )


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
