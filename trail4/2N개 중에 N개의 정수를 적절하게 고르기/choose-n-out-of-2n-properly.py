n = int(input())
num = list(map(int, input().split()))

import sys

total = sum(num)

cluster= []


num.sort()

min_gap = sys.maxsize

def select(a):
    global cluster
    global min_gap

    if len(cluster) == n:
        temp = sum(cluster)
        min_gap = min(min_gap, abs(total - temp - temp))
        return


    for i in range(a, 2 * n):
        cluster.append(num[i])
        select(i + 1)
        cluster.pop()
    





select(0)

print(min_gap)
# Please write your code here.
