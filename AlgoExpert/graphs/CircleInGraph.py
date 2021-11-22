testcases = [
    {
        'input': [
            [1, 3],
            [2, 3, 4],
            [0],
            [],
            [2, 5],
            [],
        ],
        'output': True,
    },
    {
        'input': [
            [],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0],
        ],
        'output': False,
    },
]


def cycleInGraph(edges):
    for i in range(len(edges)):
        queue = [[i, j] for j in edges[i]]
        while queue:
            path = queue.pop()
            for move in edges[path[-1]]:
                if move in path:
                    return True
                new = path.copy() + [move]
                queue.append(new)
    return False


if __name__ == '__main__':
    for case in testcases:
        ret = cycleInGraph(case['input'])
        assert(ret == case['output'])
