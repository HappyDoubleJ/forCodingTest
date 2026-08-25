n, m = map(int, input().split())

#1부터
edges = [tuple(map(int, input().split())) for _ in range(m)]


visited = [False for _ in range(n)]
visited[0] = True

#0부터
grid = [[0 for _ in range(n)] for _ in range(n)]

for i,j in edges:
    grid[i - 1][j - 1] = 1
    grid[j - 1][i - 1] = 1



#0부터
def trip(start_node):



    for idx, edge  in zip(range(n), grid[start_node]):
    
        if edge == 1 and visited[idx] == False:
            visited[idx] = True
            trip(idx)


trip(0)


cnt = 0

for i in visited:
    if i == True:
        cnt += 1

print(cnt - 1)









