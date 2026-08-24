n = int(input())


selected = set()
result = []


def select():

    if len(result) == n:
        print (*result)
        return



    for i in range(1, n + 1):
        if i not in selected:
            result.append(i)
            selected.add(i)
            select()
            result.pop()
            selected.remove(i)


select()


# Please write your code here.
