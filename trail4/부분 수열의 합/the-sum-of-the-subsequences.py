n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (m + 1)
dp[0] = True

for x in a:
    for j in range(m, x - 1, -1):  # 큰 쪽부터 거꾸로
        if dp[j - x]:
            dp[j] = True

print("Yes" if dp[m] else "No")