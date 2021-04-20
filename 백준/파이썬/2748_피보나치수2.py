def pibonachi():
    for idx in range(2, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]
    print(dp[n])

# n은 90보다 작거나 같은 자연수
n = int(input())

dp = [0] * (n + 1)
dp[1] = 1
pibonachi()