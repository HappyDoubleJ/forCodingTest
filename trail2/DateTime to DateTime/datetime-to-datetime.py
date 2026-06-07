a, b, c = map(int, input().split())

start = 10*24*60 + 11*60 + 11

end = (a-1)*24*60 + b*60 + c

print(end - start) if end >= start else print(-1)