n = int(input())

cnt = 0
def magic(N):
    global cnt

    if N == 1:
        return 0
    elif N % 2 == 0:
        cnt += 1
        return magic(N // 2)
    elif N % 2 != 0:
        cnt += 1
        return magic(N*3 + 1)
    
magic(n)

print(cnt)