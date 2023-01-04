def migratoryBirds(arr):
    types = set(arr)
    id = 0
    max_spotted = 0
    for type in types:
        if arr.count(type) > max_spotted:
            max_spotted = arr.count(type)
            id = type
    return id