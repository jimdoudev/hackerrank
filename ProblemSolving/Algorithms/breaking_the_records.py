def breakingRecords(scores):
    min_sc = scores[0]
    min_count = 0
    max_sc = scores[0]
    max_count = 0
    for score in scores:
        if score < min_sc:
            min_sc = score
            min_count += 1
        elif score > max_sc:
            max_sc = score
            max_count += 1
    return [max_count, min_count]