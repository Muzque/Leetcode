"""
Same BSTs

Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST.
Note that you're not allowed to construct any BSTs in your code.

Sample:

         10
     -----------
     8         15
   -----     -------
   5         12    94
 ---       _____  _____
 2        11      81

"""
testcases = [
    {
        'input': {
            'arrayOne': [10, 15, 8, 12, 94, 81, 5, 2, 11],
            'arrayTwo': [10, 8, 5, 15, 2, 12, 11, 94, 81]
        },
        'output': True
    }
]


def find_smaller_edges(array):
    tmp = []
    for val in array[1:]:
        if val < array[0]:
            tmp.append(val)
    return tmp


def find_bigger_edges(array):
    tmp = []
    for val in array[1:]:
        if val >= array[0]:
            tmp.append(val)
    return tmp


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False

    left1 = find_smaller_edges(arrayOne)
    left2 = find_smaller_edges(arrayTwo)
    right1 = find_bigger_edges(arrayOne)
    right2 = find_bigger_edges(arrayTwo)
    return sameBsts(left1, left2) and sameBsts(right1, right2)
