n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))


for i in range(t):
    temp_u = u[n - 1]
    temp_d = d[n - 1]

    for j in range(n - 2, -1, -1):
        u[j + 1] = u[j]
        d[j + 1] = d[j]
    u[0] = temp_d 
    d[0] = temp_u

print(*u)
print(*d)    
