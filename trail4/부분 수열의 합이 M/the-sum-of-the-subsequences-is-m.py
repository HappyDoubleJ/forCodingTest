n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
import sys

setting  = sys.maxsize

dp = [setting for _ in range(m + 1)]

dp[0] = 0



#A는 0부터 n - 1

for i in range(n):
    # A에서 거꾸로 가면... 
    for j in range(m, -1, -1):
        if A[i] <= j:
            if dp[j - A[i]] == setting:
                continue
            dp[j] = min(dp[j], dp[j - A[i]] + 1)
 



if dp[m] == setting:
    print(-1)
else:
    print(dp[m])