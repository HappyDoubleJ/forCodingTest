n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    temp_l = l[n - 1]
    temp_r = r[n - 1]
    temp_d = d[n - 1]

    # 세 배열 모두 오른쪽으로 한 칸 이동
    for j in range(n - 2, -1, -1):
        l[j + 1] = l[j]
        r[j + 1] = r[j]
        d[j + 1] = d[j]

    # 각 배열의 마지막 값이 다음 배열의 처음으로 이동
    l[0] = temp_d
    r[0] = temp_l
    d[0] = temp_r

print(*l)
print(*r)
print(*d)