def staircase(n):
    spaces = n - 1
    steps = 1
    
    for x in range(n):
        print((spaces * " ") + (steps * "#"))
        spaces -= 1
        steps +=1