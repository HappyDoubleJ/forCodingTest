MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class agent:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score


members = []
for i in range(MAX_N):
    members.append(agent(codenames[i],scores[i]))

for i in range(MAX_N):
    if members[i].score == min(scores):
        print(members[i].code_name,members[i].score)


    
