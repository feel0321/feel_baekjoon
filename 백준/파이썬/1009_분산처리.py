import sys

t = int(sys.stdin.readline())

data = dict()
data[2] = [6, 2, 4, 8]
data[3] = [1, 3, 9, 7]
data[4] = [6, 4]
data[7] = [1, 7, 9, 3]
data[8] = [6, 8, 4, 2]
data[9] = [1, 9]
#0, 1, 5, 6
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [2, 3, 7, 8]:
        print(data[a][b % 4])
    elif a in [4, 9]:
        print(data[a][b % 2])