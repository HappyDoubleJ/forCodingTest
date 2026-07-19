import sys

INT_MIN = -sys.maxsize

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

board = [
    [0 for _ in range(m)]
    for _ in range(n)
]


# 겹침 확인용 보드 초기화
def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0


# 꼭짓점 (x1, y1), (x2, y2)로 만들어지는 직사각형을 칠함
def draw(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] += 1


# 같은 칸이 두 번 칠해졌는지 확인
def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True

    return False


# 두 직사각형이 겹치는지 확인
def overlapped(
    x1, y1, x2, y2,
    x3, y3, x4, y4
):
    clear_board()

    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)

    return check_board()


# 꼭짓점 (x1, y1), (x2, y2)로 만들어지는 직사각형의 합
def rect_sum(x1, y1, x2, y2):
    total = 0

    for i in range(x1, x2):
        for j in range(y1, y2):
            total += grid[i][j]

    return total


# 첫 번째 직사각형이 정해졌을 때
# 가능한 두 번째 직사각형을 모두 확인
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN

    first_sum = rect_sum(x1, y1, x2, y2)

    # 두 번째 직사각형의 왼쪽 위 꼭짓점
    for x3 in range(n):
        for y3 in range(m):

            # 두 번째 직사각형의 오른쪽 아래 꼭짓점
            for x4 in range(x3 + 1, n + 1):
                for y4 in range(y3 + 1, m + 1):

                    if not overlapped(
                        x1, y1, x2, y2,
                        x3, y3, x4, y4
                    ):
                        second_sum = rect_sum(x3, y3, x4, y4)

                        max_sum = max(
                            max_sum,
                            first_sum + second_sum
                        )

    return max_sum


# 첫 번째 직사각형의 모든 경우 확인
def find_max_sum():
    max_sum = INT_MIN

    # 첫 번째 직사각형의 왼쪽 위 꼭짓점
    for x1 in range(n):
        for y1 in range(m):

            # 첫 번째 직사각형의 오른쪽 아래 꼭짓점
            for x2 in range(x1 + 1, n + 1):
                for y2 in range(y1 + 1, m + 1):

                    current_sum = find_max_sum_with_rect(
                        x1, y1, x2, y2
                    )

                    max_sum = max(max_sum, current_sum)

    return max_sum


answer = find_max_sum()
print(answer)