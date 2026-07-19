
import sys

INT_MIN = -sys.maxsize

# 입력
n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 두 직사각형이 칠해진 횟수를 기록하는 보드
board = [
    [0 for _ in range(m)]
    for _ in range(n)
]


# board를 전부 0으로 초기화
def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0


# (x1, y1)부터 (x2, y2)까지의 직사각형을 board에 표시
def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1


# 두 번 이상 칠해진 칸이 있는지 검사
def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True

    return False


# 두 직사각형이 겹치는지 검사
#
# 첫 번째 직사각형:
# (x1, y1) ~ (x2, y2)
#
# 두 번째 직사각형:
# (x3, y3) ~ (x4, y4)
def overlapped(x1, y1, x2, y2,
               x3, y3, x4, y4):

    clear_board()

    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)

    return check_board()


# 한 직사각형 내부 숫자의 합
def rect_sum(x1, y1, x2, y2):
    total = 0

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            total += grid[i][j]

    return total


# 첫 번째 직사각형이 정해졌을 때,
# 겹치지 않는 두 번째 직사각형을 골라 최대 합을 반환
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN

    # 두 번째 직사각형의 왼쪽 위 꼭짓점: (i, j)
    for i in range(n):
        for j in range(m):

            # 두 번째 직사각형의 오른쪽 아래 꼭짓점: (k, l)
            for k in range(i, n):
                for l in range(j, m):

                    # 두 직사각형이 겹치지 않는 경우
                    if not overlapped(
                        x1, y1, x2, y2,
                        i, j, k, l
                    ):
                        first_sum = rect_sum(x1, y1, x2, y2)
                        second_sum = rect_sum(i, j, k, l)

                        max_sum = max(
                            max_sum,
                            first_sum + second_sum
                        )

    return max_sum


# 첫 번째 직사각형도 모든 경우를 확인
def find_max_sum():
    max_sum = INT_MIN

    # 첫 번째 직사각형의 왼쪽 위 꼭짓점: (i, j)
    for i in range(n):
        for j in range(m):

            # 첫 번째 직사각형의 오른쪽 아래 꼭짓점: (k, l)
            for k in range(i, n):
                for l in range(j, m):

                    current_sum = find_max_sum_with_rect(
                        i, j, k, l
                    )

                    max_sum = max(max_sum, current_sum)

    return max_sum


answer = find_max_sum()
print(answer)