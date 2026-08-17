import sys

expression = input()

arr = []

def cal(a, b, c):
    if b == '+':
        return a + c
    if b == '-':
        return a - c
    if b == '*':
        return a * c


def cal_exp():
    mapping = {
        'a': arr[0],
        'b': arr[1],
        'c': arr[2],
        'd': arr[3],
        'e': arr[4],
        'f': arr[5],
    }

    current = mapping[expression[0]]

    for i in range(0, len(expression) - 2, 2):
        current = cal(
            current,
            expression[i + 1],
            mapping[expression[i + 2]]
        )

    return current


max_r = -sys.maxsize


def mark(idx):
    global max_r

    if idx == 6:
        current_result = cal_exp()
        max_r = max(max_r, current_result)
        return

    for num in range(1, 5):
        arr.append(num)

        mark(idx + 1)

        arr.pop()


mark(0)

print(max_r)