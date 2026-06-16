N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]


# 학생 별 카운트

counts = [0 for i in range(N+1)]

def simul():
    global N
    global student
    global K
    for i in range(M):
        counts[student[i]] += 1
        for j in range(1, N + 1):
            if counts[j] >= K:
                return j
    
    return -1


print(simul())
        

    

