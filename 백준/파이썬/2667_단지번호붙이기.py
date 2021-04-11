import sys

def dfs(idx1, idx2):
    if idx1 < 0 or idx1 >= size or idx2 < 0 or idx2 >= size:
        return False
    if minimap[idx1][idx2] == 1:
        minimap[idx1][idx2] = 0
        visited.append((idx1, idx2))
        for idx3 in range(4):
            n_idx1 = idx1 + dx[idx3]
            n_idx2 = idx2 + dy[idx3]
            if (n_idx1, n_idx2) not in visited:
                dfs(n_idx1, n_idx2)
    return True

size = int(sys.stdin.readline().rstrip())
minimap = []
answer = []
for _ in range(size):
    minimap.append(list(map(int, sys.stdin.readline().rstrip())))

# 4방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# (0, 0)부터 탐색
for idx1 in range(size):
    for idx2 in range(size):
        visited = []
        if dfs(idx1, idx2) and visited:
            answer.append(visited)
# 단지 오름차순 정렬
answer.sort(key = len)
# 단지 개수 출력
print(len(answer))
# 단지에 속한 집 개수 출력
for ans in answer:
    print(len(ans))