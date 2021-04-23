from sys import stdin
import heapq
input = stdin.readline

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        # distance 리스트와 비교하여 불필요하면 다음루프
        if distance[now] < dist:
            continue
        for idx, val in graph[now]:
            temp = dist + val
            if temp < distance[idx]:
                distance[idx] = temp
                heapq.heappush(q, (temp, idx))

v, e = map(int, input().split())
distance = [float('inf')] * (v + 1)
start = int(input())
distance[start] = 0
visited = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    command = list(map(int, input().split()))
    graph[command[0]].append((command[1], command[2]))

dijkstra(start)

for idx in range(1, v + 1):
    print('INF' if distance[idx] == float('inf') else distance[idx])