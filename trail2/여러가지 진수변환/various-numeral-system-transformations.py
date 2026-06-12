N, B = map(int, input().split())

a= []
def T2B (x, y):
    global a

    if x < y:
        a.append(x)
        return a
    
    T2B(x // y, y)
    a.append(x % y)

    return a


print(*T2B(N, B), sep = "")