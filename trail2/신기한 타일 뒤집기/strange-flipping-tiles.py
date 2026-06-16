n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
current = 100000
b_sum = 0
w_sum = 0
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

class tile:
    def __init__ (self, color):
        self.color = color

tiles = [tile('N') for _ in range(200000)]

def flip(amount, direction):
    global current

    if direction == "R":
        for i in range(current , current + amount):
            tiles[i].color = 'B'
        current = current + amount - 1
    
    else:
        for i in range(current, current - amount, -1):
            tiles[i].color = 'W'
        current = current - amount + 1

for i in range(n):
    flip(x[i],dir[i])

for i in tiles:
    if i.color == "B":
        b_sum += 1
    if i.color == "W":
        w_sum += 1

print(f"{w_sum} {b_sum}")