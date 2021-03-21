import sys

length = sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))
print(str(min(nums)) + ' ' + str(max(nums)))