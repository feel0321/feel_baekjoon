from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

def bfs():
    q.append(start)
    while q:
        x = q.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if nx == target:
                return distance[x] + 1
            if distance[nx] != 0:
                distance[nx] = min(distance[nx], distance[x] + 1)
            else:
                distance[nx] = distance[x] + 1
            q.append(nx)

start, target = map(int, input().split())
#if start == target:
#    print(0)
#else:
q = deque()
distance = defaultdict(int)
print(bfs())
'''
가장 빠른 시간이 몇초인가? => BFS
이동 방향 => x-1, x+1, x * 2
'''