import sys

case = int(sys.stdin.readline())

for c in range(case):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #' + str(c + 1) + ': ' + str(a) + ' + ' + str(b) + ' = ' + str(a + b))