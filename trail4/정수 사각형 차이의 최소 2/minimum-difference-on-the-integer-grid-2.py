n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


import sys

INF = sys.maxsize

cap = min(grid[0][0], grid[n - 1][n - 1])


lows = []

for i in range(n):
    for j in range(n):
        if grid[i][j] <= cap:
            lows.append(grid[i][j])


def first(a):
    dp = [[INF for _ in range(n)] for _ in range(n)]
    dp[0][0] = grid[0][0] - a

    for i in range(1, n):
        if grid[0][i] >= a:
            dp[0][i] = max(dp[0][i - 1], grid[0][i] - a)
    

    for i in range(1, n):
        if grid[i][0] >= a:
            dp[i][0] = max(dp[i - 1][0], grid[i][0] - a)
    
    
    for i in range(1,n):
        for j in range(1,n):
            if grid[i][j] >= a:
                dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), grid[i][j] - a)
    
    return dp[n - 1][n - 1]


min_gap = sys.maxsize

for low in lows:
    
    

    gap = first(low)

    if gap != INF:
        min_gap = min(min_gap, gap)


print(min_gap)




    


