N = int(input())
M = list(map(int, input().split()))

def change(list):
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list[i] = list[i] // 2

change(M)

for i in M:
    print(i, end=" ")




# Please write your code here.