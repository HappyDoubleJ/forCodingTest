n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

while True:
    temp = [0] * len(numbers)

    # 터질 구간 찾기
    i = 0
    while i < len(numbers):
        cnt = 1

        while i + cnt < len(numbers) and numbers[i] == numbers[i + cnt]:
            cnt += 1

        if cnt >= m:
            for j in range(i, i + cnt):
                temp[j] = 1

        i += cnt

    # 더 이상 터질 게 없으면 종료
    if sum(temp) == 0:
        break

    # 폭발 + 중력
    new_numbers = []

    for i in range(len(numbers)):
        if temp[i] == 0:
            new_numbers.append(numbers[i])

    numbers = new_numbers

print(len(numbers))
for num in numbers:
    print(num)