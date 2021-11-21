cases = [
    {
        'input': [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ],
        'output': [1, 2, 2, 2, 5],
    },
]


def get_connections(i, j, matrix, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    connections = []
    for d in directions:
        y, x = i + d[0], j + d[1]
        if len(matrix) > y >= 0 and len(matrix[y]) > x >= 0 and not visited[y][x]:
            connections.append((y, x))
    return connections


def riverSizes(matrix):
    visited = [[0 for _ in row] for row in matrix]
    results = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j] == 0:
                traverseNode(i, j, matrix, visited, results)
    return results


def traverseNode(i, j, matrix, visited, results):
    length = 0
    queue = [(i, j)]
    while queue:
        y, x = queue.pop()
        if visited[y][x] == 1:
            continue
        visited[y][x] = 1
        if matrix[y][x] == 1:
            length += 1
            queue += get_connections(y, x, matrix, visited)
    if length > 0:
        results.append(length)


if __name__ == '__main__':
    for case in cases:
        ret = riverSizes(case['input'])
        ret.sort()
        assert(ret == case['output'])
