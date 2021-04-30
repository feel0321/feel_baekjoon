from sys import stdin
input = stdin.readline

def round_(n):
    return int(n) + (1 if n - int(n) >= 0.5 else 0)

# 0 <= n <= 3 x 10^5
n = int(input())
if n == 0:
    print(0)
    exit()
exception = round_(n * 0.15)
# 1 <= 난이도 의견 <= 30
scores = [int(input()) for _ in range(n)]
scores.sort()
scores = scores[exception:len(scores)-exception]
print(round_(sum(scores) / len(scores)))