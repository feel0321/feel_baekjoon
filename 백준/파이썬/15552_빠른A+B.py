import sys

case = int(sys.stdin.readline())

for _ in range(case):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)