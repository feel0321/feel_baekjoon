import sys

case = int(sys.stdin.readline())

for idx in range(case):
    command = sys.stdin.readline().rstrip()
    left = result = 0
    right = 1
    while right <= len(command):
        test = command[left:right]
        if 'X' not in test: #다 O면
            result += test.count('O')
        else:#X가 있으면
            left = right
        right += 1
    print(result)