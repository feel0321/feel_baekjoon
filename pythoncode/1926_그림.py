import sys
from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    answer = [[x, y]]

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or ny < 0 or nx >= row or ny >= column:
                continue
            # 그림이 있고, 방문한 적이 없으면
            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                visited[nx][ny] = 1
                answer.append([nx, ny])
                q.append([nx, ny])
    return len(answer)

row, column = map(int, sys.stdin.readline().split())
matrix = []
visited = [[0] * column for _ in range(row)]
answer = []
# 탐색하는 4방향 정의
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
for _ in range(row):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for idx1 in range(row):
    for idx2 in range(column):
        #그림이 없거나, 방문한 곳이면 다음 루프
        if matrix[idx1][idx2] == 0 or visited[idx1][idx2] == 1:
            continue
        answer.append(bfs(idx1, idx2))
print(len(answer))
# valueerror 있던 부분 그림이 없을 시 answer이 빈 리스트여서 max()에서 valueerror 발생
if answer:
    print(max(answer))
else:
    print(0)