n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
dxs,dys = [-1, 1, 0, 0] , [0, 0, -1, 1]


result = []

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


def simulate():
    global r
    global c
    current_num = a[r ][c]
    result.append(a[r][c])
    for dx, dy in zip(dxs, dys):
        if in_range(r + dx, c + dy):
            if a[r + dx][c + dy] > current_num :
                r += dx
                c += dy
                return False
    
    return True




while(1):
    is_end = simulate()

    if is_end :
        break


for a in result:
    print(a, end =" ")