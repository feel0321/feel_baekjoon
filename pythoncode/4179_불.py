from sys import stdin
from collections import deque
# sys.stdin.readline()을 이렇게 표현 가능
input = stdin.readline

def bfs():
    q.append([man[0], man[1], 0])
    distance[man[0]][man[1]] = 1
    while q:
        x, y, is_fire = q.popleft()
        # 4방향 탐색을 이렇게 표현 가능
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + dx
            ny = y + dy
            # 다음 칸이 지도 밖이면
            if nx < 0 or ny < 0 or nx >= row or ny >= column:
                # 다음 칸이 지도 밖이고, 현재 칸이 불이 아니면
                if not is_fire:
                    # 탈출
                    return distance[x][y]
                # 다음 칸이 지도 밖이고, 현재 칸이 불이면 다음 루프
                continue
            # 다음 칸이 방문한적이 없고, 벽이 아니면
            if distance[nx][ny] == 0 and minimap[nx][ny] != '#':
                # 방문 처리
                q.append([nx, ny, is_fire])
                distance[nx][ny] = distance[x][y] + 1
    return

row, column = map(int, input().split())
minimap = [list(input().strip()) for _ in range(row)]
distance = [[0] * column for _ in range(row)]
q = deque()
for idx1 in range(row):
    for idx2 in range(column):
        if minimap[idx1][idx2] == 'J':
            man = [idx1, idx2]
        elif minimap[idx1][idx2] == 'F':
            q.append([idx1, idx2, 1])
            distance[idx1][idx2] = 0
answer = bfs()
print(answer if answer else 'IMPOSSIBLE')