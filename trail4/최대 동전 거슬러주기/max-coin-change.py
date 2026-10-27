n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [-1] * (m + 1)  # -1: 정확히 만들 수 없는 금액
dp[0] = 0

for i in range(1, m + 1):
    for c in coins:
        if i >= c and dp[i - c] != -1:
            dp[i] = max(dp[i], dp[i - c] + 1)

print(dp[m])