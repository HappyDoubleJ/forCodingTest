n = int(input())
a = []
def T2T(M):
    global a

    if M < 2:
        a.append(M)
        return a

    T2T(M // 2)
    a.append(M % 2)

    return a


print(*T2T(n), sep = "")