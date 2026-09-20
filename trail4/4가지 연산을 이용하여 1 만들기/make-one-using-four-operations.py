N = int(input())


from collections import deque



# 배열을 두개를 만들 필요가 없음
#0부터 2*N - 1
visited = [False for _ in range(2*N)]
cnt_array = [0 for _ in range(2*N)]


def is_range(x):

    return 0 <= x < 2*N



def bfs():


    q = deque()


    visited[N] = True
    q.append(N)

    while(q):

        x = q.popleft()

        next = [x - 1, x + 1]
        if x % 2 == 0: next.append(x // 2)
        if x % 3 == 0: next.append(x // 3)

        for nx in next:
        
            if is_range(nx) and not visited[nx]:
                q.append(nx)
                visited[nx] = True
                cnt_array[nx] = cnt_array[x] + 1



bfs()


print(cnt_array[1])









