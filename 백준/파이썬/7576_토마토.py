import sys
from collections import deque

def bfs(tomato):
    q = deque(tomato)
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # 범위 벗어나면 다음 루프
            if nx < 0 or ny < 0 or nx >= row or ny >= column:
                continue
            # 다음 탐색할 곳이 안익은 토마토면
            if box[nx][ny] == 0:
                # 방문 처리
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])

def check(box):
    answer = -1
    for b in box:
        if 0 in b:
            return -1
        answer = max(answer, max(b))
    return answer - 1

column, row = map(int, sys.stdin.readline().split())
box = []
tomato = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(row):
    command = list(map(int, sys.stdin.readline().split()))
    box.append(command)

for idx1 in range(row):
    for idx2 in range(column):
        if box[idx1][idx2] == 1:
            tomato.append([idx1, idx2])

bfs(tomato)
print(check(box))