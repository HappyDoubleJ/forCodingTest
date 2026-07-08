N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dxs , dys = [-1, 0, 0, 1], [0, -1, 1, 0]



dest = {
    "W" : 0,
    "S" : 1,
    "N" : 2,
    "E" : 3
}


def answer ():
    x, y = 0, 0
    cnt = 0
    for i in range(N):
        for j in range(dist[i]):
            x = x + dxs[dest[dir[i]]]
            y = y + dys[dest[dir[i]]]
            cnt += 1
            if x == 0 and y == 0:
                return cnt
    return -1

print(answer())
        
    

    
