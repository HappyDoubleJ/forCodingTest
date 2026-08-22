n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

result = []


max_xor = -1


def cal(a):
    start = a[0]
    for i in range(1,len(a)):
        start = start ^ a[i]
    return start


def select(b):

    global max_xor

    if result and len(result) == m:
        max_xor = max(max_xor, cal(result))
        return
    
    for i in range(b,n):
        result.append(A[i])
        select(i + 1)
        result.pop()


select(0)

print(max_xor)




