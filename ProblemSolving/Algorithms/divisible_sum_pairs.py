from itertools import combinations

def divisibleSumPairs(n, k, ar):
    return len(list(filter(lambda x: sum(x) % k == 0, combinations(ar, 2))))