import sys
from collections import deque

def dfs(start):
    visited.append(start)
    for idx in range(dots):
        if matrix[start][idx + 1] == 1 and idx + 1 not in visited:
            dfs(idx + 1)
    return visited

def bfs(start):
    visited = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        for idx in range(dots):
            if matrix[node][idx + 1] == 1 and idx + 1 not in visited:
                visited.append(idx + 1)
                q.append(idx + 1)
    return visited

dots, lines, start = map(int, sys.stdin.readline().split())
matrix = [[0] * (dots + 1) for _ in range(dots + 1)]
visited = []

for _ in range(lines):
    command = list(map(int, sys.stdin.readline().split()))
    matrix[command[0]][command[1]] = 1
    matrix[command[1]][command[0]] = 1
print(*dfs(start))
print(*bfs(start))
'''
1 ------|
|   |   |
2   3   |
|---|---4
'''