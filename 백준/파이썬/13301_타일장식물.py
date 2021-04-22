def pibonachi(n):
    if n <= 2:
        return
    for idx in range(2, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

# 1 <= n <= 80
n = int(input())
# 1일때만 (0 + 1) * 2로 오류
if n == 1:
    print(4)
    exit()
dp = [0] * (n + 2)
dp[1] = 1
pibonachi(n + 1)
answer = (dp[n + 1] + dp[n]) * 2
print(answer)

'''
피보나치 수열
(pibonachi(n) + pibonachi(n + 1)) * 2
'''