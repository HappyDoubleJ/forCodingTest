n = int(input())

# Please write your code here.
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for root in range(1, i + 1):
        left = root - 1
        right = i - root

        dp[i] += dp[left] * dp[right]



print(dp[n])