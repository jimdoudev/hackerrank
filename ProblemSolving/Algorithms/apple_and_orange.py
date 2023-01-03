def countApplesAndOranges(s, t, a, b, apples, oranges):
    apps = 0
    for apple in apples:
        if (apple + a) in range(s, t + 1):
            apps += 1
    print(apps)
    orgs = 0
    for orange in oranges:
        if (orange + b) in range(s, t + 1):
            orgs += 1
    print(orgs)