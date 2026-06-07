n = 5
name = []
height = []
weight = []

for _ in range(n):
    a, h, w = input().split()
    name.append(a)
    height.append(int(h))
    weight.append(float(w))


class man:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

mans = []

for i in range(n):
    t = man(name[i], height[i], weight[i])
    mans.append(t)

mans_1 = sorted(mans, key = lambda x : x.name)
mans_2 = sorted(mans, key = lambda x : x.height, reverse = True)

print('name')

for i in mans_1:
    print(i.name, i.height, i.weight)

print()

print('height')
for i in mans_2:
    print(i.name, i.height, i.weight)