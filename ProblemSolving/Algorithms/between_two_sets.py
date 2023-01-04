def check_a(a, x):
    for el in a:
        if(x % el != 0):
            return False
    return True

def check_b(b, x):
    for el in b:
        if(el % x != 0):
            return False
    return True

def getTotalX(a, b):
    min = sorted(a)[0]
    max = sorted(b)[-1]
    count = 0
    for x in range(min, max + 1):
        if(check_a(a, x) and check_b(b, x)):
            count += 1
    return count