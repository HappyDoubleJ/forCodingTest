a, b = map(int, input().split())

def isPrime(N):
    for i in range (2,N):
        if N % i == 0:
            return False
    return True
            



result = 0
for i in range(a, b + 1):
    if isPrime(i):
        result = result + i

print(result)
