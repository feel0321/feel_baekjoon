import sys
import collections

q = collections.deque()
num = int(sys.stdin.readline())
for i in range(num):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        q.append(int(command.split()[1]))
    elif 'pop' in command:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif 'size' in command:
        print(len(q))
    elif 'empty' in command:
        if q:
            print(0)
        else:
            print(1)
    elif 'front' in command:
        if q:
            print(q[0])
        else:
            print(-1)
    elif 'back' in command:
        if q:
            print(q[-1])
        else:
            print(-1)