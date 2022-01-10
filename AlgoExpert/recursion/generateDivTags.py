"""
def rec(length, result, array):
    if len(array) == 0:
        return
    start, end = '<div>', '</div>'
    tmp = []
    for s in array:
        left, right = s.count(start), s.count(end)
        if right == length:
            result.append(s)
        elif left == length:
            tmp += [s+end]
        elif left > right:
            tmp += [s+start, s+end]
        else:
            tmp += [s+start]
    rec(length, result, tmp)


def generateDivTags(numberOfTags):
    result = []
    rec(numberOfTags, result, ['<div>'])
    return result
"""


def generateDivTags(numberOfTags):
    result = []
    rec(numberOfTags, numberOfTags, result, '')
    return result


def rec(opening, closing, result, string):
    if opening > 0:
        rec(opening-1, closing, result, string+'<div>')

    if opening < closing:
        rec(opening, closing-1, result, string+'</div>')

    if closing == 0:
        result.append(string)
