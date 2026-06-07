n = int(input())
sequence = list(map(int, input().split()))

class cc:
    def __init__(self, number, sq):
        self.number = number
        self.sq = sq

ccs = []       

for i in range(n):
    t = cc(sequence[i], i)
    ccs.append(t)

sorted_ccs = sorted(ccs, key = lambda x : x.number)

for i in ccs:
    p = 1
    for j in sorted_ccs:
            if i.sq == j.sq:
                print(p, end=" ")
            p += 1
