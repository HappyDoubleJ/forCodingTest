n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
reversed_nums = sorted(nums, reverse=True)

add = []

for i in range(n):
    add.append(sorted_nums[i] + reversed_nums[i])

print(max(add))