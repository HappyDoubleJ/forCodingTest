N, M = map(int, input().split())

result = []

def magic(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(i)
        magic(i + 1)
        result.pop()

magic(1)


# Please write your code here.
