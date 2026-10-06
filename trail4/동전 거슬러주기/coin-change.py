N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.

import sys

max_size = sys.maxsize


dp = [sys.maxsize for _ in range(M + 1)]


dp[0] = 0


for i in range(1, M + 1):
    for j in range(N):
        if coin[j] <= i:
            if dp[i - coin[j]] == max_size:
                continue
            
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)


if dp[M] == max_size:
    print(-1)
else:
    print(dp[M])