n = int(input())
m = list(map(int, input().split()))

# Please write your code here.

import sys

bottom = -sys.maxsize



dp = [1 for _ in range(n)]




for i in range(1, n):
    for j in range(i):
        if m[j] > m[i]:
            dp[i] = max(dp[i], dp[j] + 1)



max_cnt = 0

for a in dp:
    max_cnt = max(max_cnt, a)



print(max_cnt)

