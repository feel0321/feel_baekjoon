import sys

num = int(sys.stdin.readline())
nums = []
for _ in range(num):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for num in nums:
    print(num)