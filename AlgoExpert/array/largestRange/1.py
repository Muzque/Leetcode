def largestRange(array):
    array.sort()
    h = len(array)
    mid = int(h/2) if h % 2 == 0 else int(h/2)+1
    left, right = array[0], array[h-1]
    for i in range(1, mid):
        j = h - i - 1
        if array[i] not in (array[i-1], array[i - 1]+1):
            left = array[i]
        if array[j] not in (array[j+1], array[j + 1]-1):
            right = array[j]
    return [left, right]
