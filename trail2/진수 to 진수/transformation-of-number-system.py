a, b = map(int, input().split())
n = input()

t = []
def A2T (N, A):
    sum = 0
    for i in range(len(N)):
        sum = sum * A + int(N[i])
    return sum



def T2B (N, B):
    global t
    if N < B:
        t.append(N)
        return t
    T2B(N // B, B)
    t.append(N % B)
    return t

print(*T2B(A2T(n, a), b), sep = "")