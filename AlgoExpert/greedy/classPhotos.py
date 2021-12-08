"""

"""
testcases = [
    {
        'input': (
            [5, 8, 1, 3, 4],
            [6, 9, 2, 4, 5]
        ),
        'output': True,
    },
    {
        'input': (
            [1, 3],
            [1, 2]
        ),
        'output': False,
    },
]


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    redHigher = redShirtHeights[0] > blueShirtHeights[0]
    for i in range(len(redShirtHeights)):
        diff = redShirtHeights[i] - blueShirtHeights[i]
        if not ((diff > 0 and redHigher) or (diff < 0 and not redHigher)):
            return False
    return True


if __name__ == '__main__':
    for tc in testcases:
        ret = classPhotos(*tc['input'])
        print(ret, tc['output'], tc['input'])
        assert(ret == tc['output'])
