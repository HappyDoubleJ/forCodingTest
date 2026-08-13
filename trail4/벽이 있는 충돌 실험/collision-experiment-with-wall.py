T = int(input())


dxs, dys = [-1, 0, 1, 0] , [0, -1, 0, 1]

for _ in range(T):
    N, M = map(int, input().split())
    x, y, d = [], [], []
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        d.append(di)
    
    mapping = {
    'U' : 0,
    'D' : 2,
    'L' : 1,
    'R' : 3
}

    reverse_mapping = {
        0 : "U",
        2 : "D",
        1 : "L",
        3 : "R"
    }
    marble_grid = [[0 for _ in range(N)] for _ in range(N)]
    vector_grid = [[0 for _ in range(N)] for _ in range(N)]
    temp_marble_grid = [[0 for _ in range(N)] for _ in range(N)]
    temp_vector_grid = [[0 for _ in range(N)] for _ in range(N)]

    def is_range(a, b):
        return 0 <= a < N and 0 <= b < N

    for i in range(M):
        marble_grid[x[i] - 1][y[i] - 1] = 1

    for i in range(M):
        vector_grid[x[i] - 1][y[i] - 1] = d[i]

    def move():
        for i in range(N):
            for j in range(N):
                if marble_grid[i][j] == 1:
                    if is_range(i + dxs[mapping[vector_grid[i][j]]], j + dys[mapping[vector_grid[i][j]]]):
                        temp_marble_grid[i + dxs[mapping[vector_grid[i][j]]]][j + dys[mapping[vector_grid[i][j]]]] += 1
                        temp_vector_grid[i + dxs[mapping[vector_grid[i][j]]]][j + dys[mapping[vector_grid[i][j]]]] = vector_grid[i][j]
                    else: 
                        temp_vector_grid[i][j] = reverse_mapping[(mapping[vector_grid[i][j]] + 2) % 4]
                        temp_marble_grid[i][j] += 1

                
        for i in range(N):
            for j in range(N):
                if temp_marble_grid[i][j] > 1:
                    temp_marble_grid[i][j] = 0
                    temp_vector_grid[i][j] = 0
        
        for i in range(N):
            for j in range(N):
                marble_grid[i][j] = temp_marble_grid[i][j]
        
        for i in range(N):
            for j in range(N):
                temp_marble_grid[i][j] = 0

        for i in range(N):
            for j in range(N):
                vector_grid[i][j] = temp_vector_grid[i][j]
        
        for i in range(N):
            for j in range(N):
                temp_vector_grid[i][j] = 0


    cnt = 0

    for o in range(2* N):
        cnt = 0
        move()
        for i in range(N):
            for j in range(N):
                if marble_grid[i][j] == 1:
                    cnt += 1
    print(cnt)

        # Please write your code here.




    
    


