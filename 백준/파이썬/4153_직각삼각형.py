from sys import stdin
input = stdin.readline

while 1:
    command = list(map(int, input().split()))
    if command == [0, 0, 0]:
        break
    command.sort()
    x, y, z = command
    if z ** 2 == x ** 2 + y ** 2:
        print('right')
        continue
    print('wrong')