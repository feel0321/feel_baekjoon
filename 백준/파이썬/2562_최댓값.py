import sys

nums = []
for _ in range(9):
    nums.append(int(sys.stdin.readline()))
big = max(nums)
print(big)
print(nums.index(big) + 1)