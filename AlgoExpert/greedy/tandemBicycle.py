"""

"""
testcases = [
    {
        'input': (
            [5, 5, 3, 9, 2],
            [3, 6, 7, 2, 1],
            True,
        ),
        'output': 32,
    },
]


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort(reverse=False)
    blueShirtSpeeds.sort(reverse=fastest)
    maxSpeed = 0
    for i in range(len(redShirtSpeeds)):
        maxSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return maxSpeed


if __name__ == "__main__":
    for tc in testcases:
        ret = tandemBicycle(*tc['input'])
        assert(ret == tc['output'])
