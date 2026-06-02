N = int(input())

def magic(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    return magic(N//3) + magic(N - 1)

print(magic(N))