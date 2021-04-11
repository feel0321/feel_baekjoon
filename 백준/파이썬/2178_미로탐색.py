import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        #4방향 탐색
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # 범위를 벗어나면 다음 루프
            if nx < 0 or ny < 0 or nx >= row or ny >= column:
                continue
            # 처음 방문하면
            if minimap[nx][ny] == 1:
                # 방문 처리
                minimap[nx][ny] = minimap[x][y] + 1
                # q에 넣어서 다음 탐색
                q.append((nx, ny))
    # 마지막 row, 마지막 column번쨰 값 리턴
    return minimap[row - 1][-1]

row, column = map(int, sys.stdin.readline().split())
minimap = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(row):
    minimap.append(list(map(int, sys.stdin.readline().rstrip())))
print(bfs(0, 0))
