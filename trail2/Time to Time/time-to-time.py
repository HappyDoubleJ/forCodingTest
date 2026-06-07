a, b, c, d = map(int, input().split())

def magic(x ,y):
    return x * 60 + y

print(magic(c,d) -magic(a, b))