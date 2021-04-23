from sys import stdin
input = stdin.readline

def check(n):
    if n >= 2:
        dp[2] = point[1] + point[2]
    for idx in range(3, n + 1):
        # 한 칸 전진과 두 칸 전진중에 큰 값
        dp[idx] = max(dp[idx - 3] + point[idx - 1] + point[idx], dp[idx - 2] + point[idx])
    return dp[n]

n = int(input())
point = [0]
for _ in range(n):
    point.append(int(input()))
dp = [0] * (n + 1)
dp[1] = point[1]

print(check(n))
print('point : ', point)
print('dp : ', dp)
'''
한칸 or 두칸 전진
세칸 연속 불가

마지막 3을 무조건 밟아야 하면 아래 2경우처럼 존재
0 1 2 3
1. 마지막 계단의 전 계단을 밟음 (한 칸 전진) => 세칸 연속이 안되니까 두 칸 전은 밟지않음
? ? O O => O X O O
2. 마지막 계단의 전 계단을 밟지 않음 (두 칸 전진)
? ? X O => O O X O
'''