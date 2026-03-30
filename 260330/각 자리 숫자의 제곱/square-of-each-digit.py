N = int(input())

def magic(n):
    if n == 0:
        return 0 

    return (n % 10) * (n % 10) + magic(n // 10)

print(magic(N))