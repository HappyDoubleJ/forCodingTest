user2_id, user2_level = input().split()
user2_level = int(user2_level)


class member:
    def __init__(self, id, level):
        self.id = id
        self.level = level
    


member1 = member('codetree', 10)
member2 = member(user2_id, user2_level)

print(f'user {member1.id} lv {member1.level}')
print(f'user {member2.id} lv {member2.level}')
