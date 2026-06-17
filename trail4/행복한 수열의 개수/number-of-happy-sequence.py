n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


cnt = 0
answer_row = 0
answer_col = 0
#행 세게
def count_row(grid_A):
    global cnt
    global answer_row
    if m == 1:
        return n
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if grid_A[i][j] == grid_A[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= m:
                answer_row += 1
                break
    
    return answer_row


def count_col(grid_A):
    global cnt
    global answer_col
    if m == 1:
        return n
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if grid_A[j][i] == grid_A[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= m:
                answer_col += 1
                break
    
    return answer_col


print(count_row(grid) + count_col(grid))