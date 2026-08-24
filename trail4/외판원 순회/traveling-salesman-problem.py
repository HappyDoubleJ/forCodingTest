n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

import sys


selected_set = set()
selected = []
min_result = sys.maxsize


def select():
    global min_result


    if len(selected) == n - 1:
        temp_result = A[0][selected[0]] + A[selected[n - 2]][0]
        temp_distance = set()
        temp_distance.add(A[0][selected[0]])
        temp_distance.add(A[selected[n - 2]][0])

        for i in range(n - 2):
            temp_result += A[selected[i]][selected[i + 1]]
            temp_distance.add(A[selected[i]][selected[i + 1]])
        if 0 not in temp_distance:
            min_result = min(temp_result, min_result)
        return
            


    for i in range(1, n):

        if i not in selected_set:
            selected.append(i)
            selected_set.add(i)
            select()
            selected.pop()
            selected_set.remove(i)




select()

print(min_result)