import sys

nums = []
for idx in range(10):
    nums.append(int(sys.stdin.readline()) % 42)
nums = set(nums)
print(len(nums))

'''
import sys
from collections import Counter

nums = []
for idx in range(10):
    nums.append(int(sys.stdin.readline()) % 42)
nums = Counter(nums)
print(len(nums))
'''