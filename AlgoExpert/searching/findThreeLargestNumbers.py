"""

"""
testcases = [
    {
        'input': {
            "array": [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
        },
        'output': [18, 141, 541]
    },
    {
        'input': {
            "array": [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
        },
        'output': [-2, -1, 7]
    },
]


from lib import run_tests


"""
def findThreeLargestNumbers(array):
    ret = [float('-inf') for _ in range(3)]
    for num in array:
        tmp = min(ret)
        if num < tmp:
            continue
        ret.remove(tmp)
        ret.append(num)
    return sorted(ret)
"""

"""
def findThreeLargestNumbers(array):
    a, b, c = (float('-inf') for _ in range(3))
    for num in array:
        if num > a:
            b, c = a, b
            a = num
        elif num > b:
            c = b
            b = num
        elif num > c:
            c = num
    return [c, b, a]
"""


def reorder_array(array, index, num):
    for i in range(index):
        array[i] = array[i+1]
    array[index] = num


def update_return_array(array, num):
    if num > array[2]:
        reorder_array(array, 2, num)
    elif num > array[1]:
        reorder_array(array, 1, num)
    elif num > array[0]:
        reorder_array(array, 0, num)


def findThreeLargestNumbers(array):
    ret = [float('-inf') for _ in range(3)]
    for num in array:
        update_return_array(ret, num)
    return ret


def main():
    run_tests(
        testcases=testcases,
        function=findThreeLargestNumbers,
    )
