n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]



points.sort(key = lambda x : abs(x[1][0]) + abs(x[1][1]))

for i in points:
    print(i[0] + 1)


#번호를 출력해야 하느데..