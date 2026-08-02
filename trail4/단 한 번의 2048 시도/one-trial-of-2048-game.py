# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
none = -1




temp_grid = [[0 for _ in range(4)] for _ in range(4)]


def rotate():
    for i in range(4):
        for j in range(4):
            temp_grid[i][j] = grid[4 - j - 1][i]
    for i in range(4):
        for j in range(4):
            grid[i][j] = temp_grid[i][j]
    

def move():
    for i in range(4):
        for j in range(4):
            temp_grid[i][j] = 0
    #열
    for i in range(4):
        target_row = 3
        hand = none
        #행
        for j in range(3, -1, -1):
            #0일때
            if grid[j][i] == 0:
                continue
            #0이 아니고 합쳐질 때
            elif grid[j][i] == hand:
                temp_grid[target_row][i] = hand * 2
                hand = none
                target_row -= 1
            #0이 아니고 합쳐지지 않을 때
            elif hand != none:
                temp_grid[target_row][i] = hand
                hand = grid[j][i]
                target_row -= 1
            else:
                hand = grid[j][i]
        if hand != none:                     
            temp_grid[target_row][i] = hand
    for i in range(4):
        for j in range(4):
            grid[i][j] = temp_grid[i][j]


rotate_count = {
    'U' : 2,
    'D' : 0,
    'R' : 1,
    'L' : 3
}

for i in range(rotate_count[dir]):
    rotate()


move()

for i in range(4 - rotate_count[dir]):
    rotate()

for row in grid:
    print(*row)