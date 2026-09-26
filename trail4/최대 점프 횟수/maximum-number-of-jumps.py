n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


import sys
bottom = - sys.maxsize

dp = [bottom for _ in range(n)]

dp[0] = 0


for i in range(1,n):
    for j in range(0, i):
        if dp[j] == bottom:
            continue

        if arr[j] + j >= i:
            dp[i] = max(dp[i], dp[j] + 1)



max_cnt = 0

for a in dp:
    max_cnt = max(max_cnt, a)



print(max_cnt)

