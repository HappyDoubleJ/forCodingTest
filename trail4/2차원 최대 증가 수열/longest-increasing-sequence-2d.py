n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


import sys
# Please write your code here.

bottom = -sys.maxsize

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n


dp = [[bottom for _ in range(m)] for _ in range(n)]


dp[0][0] = 1


#4중 for 문..?


for i in range(n):
    for j in range(m):
        for k in range(i):
            for l in range(j):

                if dp[k][l] == bottom:
                    continue
                
                if i - k >= 1 and j - l >= 1 and grid[k][l] < grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[k][l] + 1)



max_cnt = 0

for i in range(n):
    for j in range(m):
        max_cnt = max(max_cnt, dp[i][j])


print(max_cnt)
