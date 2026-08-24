n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


import sys



selected_x = set()
result_x = []
result_y = []

max_min_sum = -1

def select(y):
    global max_min_sum


    if len(result_x) == n:
        temp_min_sum = sys.maxsize
        for i, j in zip(result_x, result_y):
            temp_min_sum = min(grid[i][j] , temp_min_sum)
        max_min_sum = max(max_min_sum, temp_min_sum)

        




    for i in range(n):
        if i not in selected_x:
            selected_x.add(i)
            result_x.append(i)
            result_y.append(y)
            select(y + 1)
            selected_x.remove(i)
            result_x.pop()
            result_y.pop()



select(0)
print(max_min_sum)