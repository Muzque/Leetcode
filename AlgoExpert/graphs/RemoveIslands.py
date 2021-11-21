cases = [
    {
        "input": [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ],
        "output": [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ],
    },
]


def initQueue(matrix):
    h = len(matrix)
    top = [(0, j) for j in range(len(matrix[0]))]
    bot = [(len(matrix) - 1, j) for j in range(len(matrix[h - 1]))]
    left = [(i, 0) for i in range(h)]
    right = [(i, len(matrix[i])-1) for i in range(h)]
    return top + bot + left + right


def get_connections(i, j, matrix, visited):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    connections = []
    for d in directions:
        y, x = i + d[0], j + d[1]
        if len(matrix) > y >= 0 and len(matrix[y]) > x >= 0 and not visited[y][x]:
            connections.append((y, x))
    return connections


def removeIslands(matrix):
    visited = [[False for _ in range(len(row))] for row in matrix]
    queue = initQueue(matrix)
    while queue:
        i, j = queue.pop()
        if visited[i][j] is True:
            continue
        visited[i][j] = True
        if matrix[i][j] == 1:
            queue += get_connections(i, j, matrix, visited)
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if not visited[i][j]:
                matrix[i][j] = 0
    return matrix


if __name__ == '__main__':
    for case in cases:
        ret = removeIslands(case['input'])
        assert(ret == case['output'])
