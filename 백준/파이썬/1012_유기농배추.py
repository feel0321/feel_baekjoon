import sys
#재귀 한도 설정 => 이거 해야 백준 재귀 런타임 에러가 안남
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= row or y >= column:
        return False
    if minimap[x][y] == 1:
        minimap[x][y] = 0
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            dfs(nx, ny)
    return True

test = int(sys.stdin.readline())
# 4방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(test):
    answer = []
    count = 0
    row, column, target = map(int, sys.stdin.readline().split())
    minimap = [[0] * column for _ in range(row)]
    for __ in range(target):
        command = list(map(int, sys.stdin.readline().split()))
        minimap[command[0]][command[1]] = 1
    
    for idx1 in range(row):
        for idx2 in range(column):
            if minimap[idx1][idx2] == 1:
                dfs(idx1, idx2)
                count += 1
    print(count)