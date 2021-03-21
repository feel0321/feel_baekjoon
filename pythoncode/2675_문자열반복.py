import sys

case = int(sys.stdin.readline())

for _ in range(case):
    command = sys.stdin.readline().split()
    for c in command[1]:
        print(c * int(command[0]), end = '')
    print()