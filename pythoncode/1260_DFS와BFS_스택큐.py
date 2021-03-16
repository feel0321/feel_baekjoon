import sys
import collections
'''
1--2--|
 |-3--|
 |----4
'''
def dfs(graph, idx):
    visited = []
    stack = []
    stack.append(idx)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node][::-1])
    print(*visited)

def bfs(graph, idx):
    visited = []
    q = collections.deque()
    q.append(idx)
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    print(*visited)

_, num, idx = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(num):
    start, end = map(int, sys.stdin.readline().split())
    if end not in graph[start]:
        graph[start].append(end)
    if start not in graph[end]:
        graph[end].append(start)
for key in graph.keys():
    graph[key].sort()
dfs(graph, idx)
bfs(graph, idx)