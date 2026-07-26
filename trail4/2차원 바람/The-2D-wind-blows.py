n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]


map_A = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        map_A[i][j] = a[i][j]


map_temp = [[0 for _ in range(m)] for _ in range (n)]


#행렬은 다 -1 해야 함

#0 <= y1, y2 <= n - 1

def shift_box (x1,y1, x2,y2):
    
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    temp_row_up = map_A[x1][y2]
    temp_row_down = map_A[x2][y1]
    temp_col_left = map_A[x1 + 1][y1]
    temp_col_right = map_A[x2 - 1][y2]

    for i in range(y2, y1, -1):
        map_A[x1][i] = map_A[x1][i - 1]
    for i in range(x2 - 1, x1 + 1, -1):
        map_A[i][y2] = map_A[i - 1][y2]
    for i in range(y1, y2):
        map_A[x2][i] = map_A[x2][i + 1]
    for i in range(x1 + 1,x2 - 1): 
        map_A[i][y1] = map_A[i + 1][y1]
    
    map_A[x1 + 1][y2] = temp_row_up
    map_A[x2 - 1][y1] = temp_row_down
    map_A[x1][y1] = temp_col_left
    map_A[x2][y2] = temp_col_right


def is_range(x1,y1):
    return 0 <= x1 and x1 < n and 0 <= y1 and y1 < m 

def sig (x1,y1, x2,y2):
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    
    for i in range(x1,x2 + 1):
        for j in range(y1, y2 + 1):
            cnt = 1
            total = map_A[i][j]
            if is_range(i, j + 1):
                total = total + map_A[i][j + 1]
                cnt += 1
            if is_range(i, j - 1):
                total = total + map_A[i][j - 1]
                cnt += 1
            if is_range(i + 1, j):
                total = total + map_A[i + 1][j]
                cnt += 1
            if is_range(i - 1, j):
                total = total + map_A[i - 1][j]
                cnt += 1
            total //= cnt
            map_temp[i][j] = total
    


for r1,c1,r2,c2 in winds:
    shift_box(r1,c1,r2,c2)
    for i in range(n):
        for j in range(m):
            map_temp[i][j] = map_A[i][j]
    sig(r1,c1,r2,c2)
    for i in range(n):
        for j in range(m):
            map_A[i][j] = map_temp[i][j]


for row in map_A:
    print(*row)