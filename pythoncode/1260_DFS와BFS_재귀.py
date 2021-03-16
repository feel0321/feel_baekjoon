import sys
import collections

def dfs(graph, idx, visited = []):
    visited.append(idx)
    for node in graph[idx]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, idx):
    visited = []
    q = collections.deque()
    q.append(idx)
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    return visited

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
print(*dfs(graph, idx))
print(*bfs(graph, idx))