n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class info:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

infos = []

for i in range (n):
    t = info(name[i], street_address[i],region[i])
    infos.append(t) 

# 이 클래스 배열을 이름을 기준으로 사전순으로 배열 해서 가장 마지막 꺼를 출력하기
infos.sort(key = lambda x:x.name)

print(f"name {infos[n - 1].name}")
print(f"addr {infos[n - 1].street_address}")
print(f"city {infos[n - 1].region}")