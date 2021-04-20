def pibonachi(k):
    for idx in range(2, k + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]
    print(dp[k - 1], dp[k])

# 1 <= K <= 45
k = int(input())
dp = [0] * (k + 1)
dp[1] = 1
pibonachi(k)
'''
        => A        => 1 0
A       => B        => 0 1
B       => BA       => 1 1
BA      => BAB      => 1 2
BAB     => BABBA    => 2 3
BABBA   => BABBABAB => 3 5

B => BA
A => B
==> 피보나치랑 같음
'''