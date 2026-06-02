n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
sorted_nums = sorted(nums)

print(sorted_nums[k - 1])