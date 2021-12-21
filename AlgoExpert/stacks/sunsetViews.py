def sunsetViews(buildings, direction):
    ret = []
    steps = (0, len(buildings), 1) if direction == 'WEST' else (len(buildings)-1, -1, -1)
    localHeight = 0
    for i in range(*steps):
        current = buildings[i]
        if current > localHeight:
            ret.append(i)
            localHeight = current
    if direction == 'EAST':
        ret.reverse()
    return ret
