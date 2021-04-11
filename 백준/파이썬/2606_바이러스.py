import sys

def dfs(start):
    visited.append(start + 1)
    for idx in range(computer):
        if graph[start][idx] == 1 and idx + 1 not in visited:
            dfs(idx)
    return visited

computer = int(sys.stdin.readline().rstrip())
line = int(sys.stdin.readline().rstrip())
graph = [[0] * computer for _ in range(computer)]
visited = []

for _ in range(line):
    command = list(map(int, sys.stdin.readline().split()))
    graph[command[0] - 1][command[1] - 1] = 1
    graph[command[1] - 1][command[0] - 1] = 1
print(*graph)
print(len(dfs(0)) - 1)