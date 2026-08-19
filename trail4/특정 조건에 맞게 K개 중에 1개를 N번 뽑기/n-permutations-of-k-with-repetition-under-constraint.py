K, N = map(int, input().split())

result = []

def sy(n, k):
    if n == 0:
        print(*result)
        return

    for i in range(1, k + 1):

        if result and i == result[-1]:
            result.append(i)

            # i 하나를 넣었더니 길이가 완성된 경우
            if n == 1:
                sy(n - 1, k)

            else:
                # 다음에는 i와 다른 숫자를 강제로 넣기
                for j in range(1, k + 1):
                    if j != i:
                        result.append(j)
                        sy(n - 2, k)
                        result.pop()

            result.pop()

        else:
            result.append(i)
            sy(n - 1, k)
            result.pop()

sy(N, K)