n = int(input())


memo = [-1 for n in range(n + 1)]


# cal(n) = cal(n - 2) + cal(n - 3)


def cal(N):

    if N == 0:
        return 1

    if N < 0 or N == 1:
        return 0

    if memo[N] != -1:
        return memo[N]

    memo[N] = cal(N - 2) + cal(N - 3)

    return memo[N]


print(cal(n) % 10007)

