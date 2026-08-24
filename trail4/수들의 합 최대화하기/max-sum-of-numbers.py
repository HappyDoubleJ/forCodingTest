n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

selected_x = set()
selected_y = set()

result_x = []
result_y = []


max_sum = -1

selected_x = set()
max_sum = -1

def select(y, current_sum):
    global max_sum

    if y == n:
        max_sum = max(max_sum, current_sum)
        return

    for i in range(n):
        if i not in selected_x:
            selected_x.add(i)

            select(y + 1, current_sum + grid[i][y])

            selected_x.remove(i)


select(0, 0)

print(max_sum)