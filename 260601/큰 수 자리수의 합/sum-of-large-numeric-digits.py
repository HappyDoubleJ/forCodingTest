a, b, c = map(int, input().split())

product = a * b * c


def magic(N):
    if N == 0:
        return 0
    return magic(N//10) + N % 10

print(magic(product))