from sys import stdin
input = stdin.readline

n = int(input())
command = list(map(int, input().split()))
answer = []

for idx in range(n):
    answer.insert(command[n - 1 - idx], n - idx)
    #print(*answer)
print(*answer)