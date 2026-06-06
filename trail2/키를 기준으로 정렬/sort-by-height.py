n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))


class man:
    def __init__ (self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

mans = []

for i in range(n):
    t = man(name[i], height[i], weight[i])
    mans.append(t)

mans.sort(key = lambda x:x.height)

for i in range(n):
    print(f'{mans[i].name} {mans[i].height} {mans[i].weight}')
