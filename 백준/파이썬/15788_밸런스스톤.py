from sys import stdin
input = stdin.readline

# 행의 합과 좌하향 대각선 확인
def check(minimap):
    temp = sum(minimap[0])
    idx1 = idx2 = 0
    x_line = 0
    while idx1 < len(minimap):
        # 행의 합이 다르면
        if temp != sum(minimap[idx1]):
            return False
        x_line += minimap[idx1][idx2]
        idx1 += 1
        idx2 += 1
    # 좌하향 대각선의 합이 다르면
    if temp != x_line:
        return False
    return True
# 열의 합과 우상향 대각선 확인
def check2(minimap):
    # 2차원 리스트 뒤집기
    minimap = list(map(list, zip(*minimap)))
    #print(*minimap)

    temp = sum(minimap[0])
    idx1 = 0
    idx2 = len(minimap) - 1
    x_line = 0
    while idx1 < len(minimap):
        # 뒤집은 후 행의 합이 다르면 (뒤집기 전의 열의 합이 다르면)
        if temp != sum(minimap[idx1]):
            return False
        x_line += minimap[idx1][idx2]
        idx1 += 1
        idx2 -= 1
    # 우상향 대각선의 합이 다르면
    if temp != x_line:
        return False
    return True

# 2 <= n <= 500
n = int(input())
minimap = [list(map(int, input().split())) for _ in range(n)]

for idx in range(n):
    if 0 in minimap[idx]:
        where_zero = idx
        where_zero2 = minimap[idx].index(0)
        break
target = sum(minimap[1]) if where_zero == 0 else sum(minimap[0])
# 정답으로 의심되는 수
answer = target - sum(minimap[where_zero])
minimap[where_zero][where_zero2] = answer
print(answer if check(minimap) and check2(minimap) else -1)