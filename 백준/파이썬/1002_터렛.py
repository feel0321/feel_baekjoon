from sys import stdin
input = stdin.readline

def check():
    # 답이 무수히 많음 => 두 원이 완벽히 겹쳐야 함 (둘의 거리 == 0 and 반지름이 같음)
    if R == 0 and r1 == r2:
        return -1
    # 답이 1 => 접점이 1개 => 외접 (둘의 거리 == 두 반지름의 합) or 내접 (둘의 거리 == ) => 그림 첨부
    elif R == r1 + r2 or R == abs(r1 - r2):
        return 1
    # 답이 2개 => 접점이 2개 => 외접 or 내접 => 그림 첨부
    elif R < r1 + r2 and R > abs(r1 - r2):
        return 2
    # 나머지. 이외 상황은 접점이 없다 => 0
    return 0

case = int(input())
for _ in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 사람의 실제 거리
    R = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    print(check())