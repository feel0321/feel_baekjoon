import sys

num = int(sys.stdin.readline())
stack = []
for _ in range(num):
    command = sys.stdin.readline().split()
    if 'push' in command:
        stack.append(int(command[1]))
    elif 'pop' in command:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if stack:
            print(0)
        else:
            print(1)
    elif 'top' in command:
        if stack:
            print(stack[-1])
        else:
            print(-1)
