N = int(input())


def sigma(N):

    if N == 1:
        return 1

    return N + sigma(N - 1)

print(sigma(N))
# Please write your code here.