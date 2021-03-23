import sys
from collections import defaultdict

num = int(sys.stdin.readline())
nums = defaultdict(int)

for _ in range(num):
    nums[int(sys.stdin.readline())] += 1
for item in sorted(nums.items()):
    for val in range(item[1]):
        print(item[0])