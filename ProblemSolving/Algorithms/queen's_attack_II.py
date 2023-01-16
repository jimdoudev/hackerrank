def possible_squares(n, q):
    moves = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
    total_moves = 0
    for move in moves:
        next_move = (q[0] + move[0], q[1] + move[1])
        # print(list(board[next_move[0]][next_move[1]]))
        while(next_move[0] <= n and next_move[0] > 0 and next_move[1] <= n and next_move[1] > 0):
            total_moves += 1
            next_move = (next_move[0] + move[0], next_move[1] + move[1])
    return total_moves

def blocks_of_interest(q, obstacles):
    int_blocks = []
    for obstacle in obstacles:
        if(obstacle[0] - q[0] == obstacle[1] - q[1]):
            int_blocks.append([obstacle[0], obstacle[1], "ne"])
        elif(q[0] - obstacle[0] == obstacle[1] > q[1]):
            int_blocks.append([obstacle[0], obstacle[1], "se"])
        elif(obstacle[0] > q[0] == q[1] - obstacle[1]):
            int_blocks.append([obstacle[0], obstacle[1], "nw"])
        elif(q[0] - obstacle[0] == q[1] - obstacle[1]):
            int_blocks.append([obstacle[0], obstacle[1], "sw"])
        elif obstacle[0] == q[0]:
            int_blocks.append([obstacle[0], obstacle[1], "y"])
        elif obstacle[1] == q[1]:
            int_blocks.append([obstacle[0], obstacle[1], "x"])
    return int_blocks


def blockedSquares(n, q, int_blocks):
    blocked = 0
    for int_block in int_blocks:
        if (int_block[2] == "ne"):
            if(n + 1 - int_block[0] >= n + 1 - int_block[1]):
                blocked += (n + 1 - int_block[1])
            else:
                blocked += (n + 1 - int_block[0])
        elif(int_block[2] == "se"):
            if(int_block[0] >= n + 1 - int_block[1]):
                blocked += (n + 1 - int_block[1])
            else:
                blocked += (int_block[0])
        elif(int_block[2] == "nw"):
            if(n + 1 - int_block[0] >= int_block[1]):
                blocked += (int_block[1])
            else:
                blocked += (n + 1 - int_block[0])
        elif(int_block[2] == "sw"):
            if(int_block[0] >= int_block[1]):
                blocked += (int_block[1])
            else:
                blocked += (int_block[0])
        elif(int_block[2] == "x"):
            if(int_block[0] > q[0]):
                blocked += ((n + 1) - int_block[0])
            else:
                blocked += (int_block[0])
        elif(int_block[2] == "y"):
            if(int_block[1] > q[1]):
                blocked += ((n + 1) - int_block[1])
            else:
                blocked += (int_block[1])
    return blocked

def queensAttack(n, k, r_q, c_q, obstacles):
    # board = [[tuple([y, x]) for x in range(1, n + 1)] for y in range(n, 0, -1)]
    q = [r_q, c_q]
    if(k == 0):
        return possible_squares(n, q)
    else:
        return possible_squares(n, q) - blockedSquares(n, q, blocks_of_interest(q, obstacles))

print(queensAttack(5, 3, 4, 3, [[5,5], [4,2], [2,3]]))
# print(blocks_of_interest((4,4), [[6,4], [7,7], [2,7], [5,3]]))
# print(blockedSquares(8, (4,4), blocks_of_interest((4,4), [[3,5]])))