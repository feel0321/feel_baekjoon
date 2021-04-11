from sys import stdin
input = stdin.readline

n = int(input().strip())
command = list(map(int, input().split()))
command.sort()
print(command[0] * command[-1])