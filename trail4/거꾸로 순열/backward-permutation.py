n = int(input())



result = []

selected = set()


def select():

    if len(result) == n:
        print(*result)
        return



    for i in range(n, 0, -1):

        if i not in selected:
            result.append(i)
            selected.add(i)
            select()
            result.pop()
            selected.remove(i)
# Please write your code here.


select()