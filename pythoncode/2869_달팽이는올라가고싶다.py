import sys

a, b, v = map(int, sys.stdin.readline().split())
day = (v - a) / (a - b)
day = int(day) if day % 1 == 0 else int(day) + 1
print(day + 1)