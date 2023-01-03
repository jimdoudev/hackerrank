def diagonalDifference(arr):
    primary, secondary = 0, 0
    max = len(arr)
    for x in range(0, max):
        primary += arr[x][x]
        secondary += arr[x][max - 1]
        max -= 1
    return abs(primary - secondary)