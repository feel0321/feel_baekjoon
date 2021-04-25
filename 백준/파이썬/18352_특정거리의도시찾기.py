from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for n_idx in graph[now]:
            if distance[n_idx] == -1:
                q.append(n_idx)
                distance[n_idx] = distance[now] + 1

# 도시 개수, 도로 개수, 거리 정보, 출발 도시
city, road, dist_target, start = map(int, input().split())
graph = [[] for _ in range(city + 1)]
distance = [-1] * (city + 1)
distance[start] = 0
for _ in range(road):
    command = list(map(int, input().split()))
    graph[command[0]].append(command[1])

bfs(start)

#print(distance)
if dist_target not in distance:
    print(-1)
    exit()
for idx in range(1, city + 1):
    if distance[idx] == dist_target:
        print(idx)