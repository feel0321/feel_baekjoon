# 1 <= m <= n <= 100만
m, n = map(int, (input().split()))
sosu = [True] * (n+1)
sosu[1] = False
for idx in range(2, n+1):
    if sosu[idx]:
        for idx2 in range(2*idx, n+1, idx):
            sosu[idx2] = False
    if idx >= m and sosu[idx]:
        print(idx)