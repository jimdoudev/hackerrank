def compareTriplets(a, b):
    scores = [0, 0]
    for x in range(0, 3):
        if a[x] > b[x]:
            scores[0] += 1
        elif b[x] > a[x]:
            scores[1] += 1
    return scores