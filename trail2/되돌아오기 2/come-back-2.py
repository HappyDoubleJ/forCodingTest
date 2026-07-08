commands = input()

dxs ,dys = [0, 1, 0, -1] , [1, 0, -1, 0] # 위 오 아 왼

dic = {
    "L" : 3,
    "R" : 1
}



def count():
    cnt = 0
    x, y = 0 , 0
    start = 0
    for i in commands:
        if i == "F":
            x,y = x + dxs[start], y + dys[start]
            cnt += 1
        else:
            start = (start + dic[i]) % 4
            cnt += 1
        if x == 0 and y == 0:
            return cnt
    return -1

print(count())


