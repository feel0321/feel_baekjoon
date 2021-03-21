import sys

test = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

big = max(score)
for idx in range(test):
    score[idx] = score[idx] / big * 100
print(sum(score) / test)