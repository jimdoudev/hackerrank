def plusMinus(arr):
    props = [0, 0, 0]
    for num in arr:
        if num > 0:
            props[0] += 1
        elif num < 0:
            props[1] += 1
        else:
            props[2] += 1
    for prop in props:
        print(round(prop/len(arr), 6))